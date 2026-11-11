#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vista cartográfica agregada de expansión urbana; NO apta para medición.

Entradas locales: huella_2018_2036.tif (10 m, EPSG:32619), límite ONE GPKG.
Salida: GeoJSON EPSG:4326. Se conserva la clase temporal modal de las celdas
urbanas de cada cuadrícula de 100 m. No reproduce exactamente la huella 10 m.
"""
import argparse
import json
from pathlib import Path

import fiona
import numpy as np
import rasterio
from pyproj import Transformer
from rasterio.features import geometry_mask, shapes
from rasterio.transform import Affine
from shapely.geometry import mapping, shape
from shapely.ops import transform as transform_geometry

YEARS = (2018, 2021, 2024, 2027, 2030, 2033, 2036)

def exportar(raster, limite, salida, resolucion=100, min_urbano=0.10):
    with fiona.open(limite) as ds_limite:
        geometrias = [feature["geometry"] for feature in ds_limite]
        if not geometrias:
            raise ValueError("El límite territorial no contiene polígonos.")
        crs_limite = ds_limite.crs

    with rasterio.open(raster) as ds:
        if ds.crs is None or ds.crs.to_epsg() != 32619:
            raise ValueError("Se espera un ráster en EPSG:32619.")
        if ds.res != (10.0, 10.0) or resolucion % 10:
            raise ValueError("Se requiere píxel de 10 m y resolución múltiplo de 10.")
        if rasterio.crs.CRS.from_user_input(crs_limite) != ds.crs:
            raise ValueError("Reproyectar primero el límite ONE al CRS del ráster.")

        pixeles = ds.read(1)
        dentro = geometry_mask(
            geometrias, out_shape=pixeles.shape, transform=ds.transform,
            invert=True
        )
        clases = pixeles[dentro]
        conteos = {str(y): int(np.count_nonzero(clases == y)) for y in YEARS}

        n = resolucion // 10
        alto, ancho = pixeles.shape
        completar = ((0, (-alto) % n), (0, (-ancho) % n))
        pixeles = np.pad(pixeles, completar, constant_values=0)
        dentro = np.pad(dentro, completar, constant_values=False)
        h, w = pixeles.shape[0] // n, pixeles.shape[1] // n
        celdas = pixeles.reshape(h, n, w, n).transpose(0, 2, 1, 3)
        celdas = celdas.reshape(h, w, n * n)
        mascara = dentro.reshape(h, n, w, n).transpose(0, 2, 1, 3)
        mascara = mascara.reshape(h, w, n * n)
        total_validos = mascara.sum(axis=2)
        por_clase = np.stack([
            np.sum((celdas == y) & mascara, axis=2) for y in YEARS
        ], axis=-1)
        total_urbano = por_clase.sum(axis=-1)
        participacion = np.divide(
            total_urbano, total_validos, out=np.zeros_like(
                total_urbano, dtype=np.float64
            ), where=total_validos > 0
        )
        usar = (total_validos >= 0.25 * n * n) & (
            participacion >= min_urbano
        )
        predominante = np.asarray(YEARS, dtype=np.int16)[
            np.argmax(por_clase, axis=-1)
        ]
        categorias = np.where(usar, predominante, 0).astype("int16")
        tr = ds.transform * Affine.scale(n, n)
        reproyectar = Transformer.from_crs(
            ds.crs, "EPSG:4326", always_xy=True
        ).transform

        elementos = []
        for geom, valor in shapes(
            categorias, mask=categorias > 0, transform=tr, connectivity=4
        ):
            anio = int(valor)
            geo = transform_geometry(reproyectar, shape(geom))
            elementos.append({
                "type": "Feature",
                "geometry": mapping(geo),
                "properties": {
                    "anio": anio,
                    "tipo": "clasificado" if anio <= 2024 else "simulado"
                }
            })
        salida = Path(salida)
        salida.parent.mkdir(parents=True, exist_ok=True)
        salida.write_text(json.dumps({
            "type": "FeatureCollection",
            "features": elementos
        }, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print("GeoJSON:", salida, "elementos:", len(elementos))
        print("Conteos EXACTOS del ráster recortado (píxeles 10 m):", conteos)
        print("ATENCIÓN: vista agregada, NO calcular superficies sobre el GeoJSON.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--raster", required=True)
    ap.add_argument("--limite", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--resolucion", type=int, default=100)
    ap.add_argument("--min-urbano", type=float, default=0.10)
    args = ap.parse_args()
    exportar(args.raster, args.limite, args.salida,
             args.resolucion, args.min_urbano)
