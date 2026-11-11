# Avances de expansión urbana de Santiago (11-11-2026)

**Estado:** preliminar para revisión técnica; **no** constituye zonificación normativa.

- `indicadores_expansion_urbana_santiago_2018_2036.csv`: conteos de píxeles de 10 m y superficie por año de primera clasificación/simulación, recortados al municipio de Santiago usando límite construido a partir de 31 secciones ONE. EPSG:32619 para el cálculo (100 m²/celda). Los años 2018, 2021 y 2024 corresponden a clasificaciones; 2027, 2030, 2033 y 2036 son escenarios tipo MOLUSCE.
- `km2_periodo` representa superficie añadida respecto del período anterior, salvo 2018, que es la superficie base. `crecimiento_periodo_pct` corresponde al intervalo trienal, no a una tasa anual.
- Coincidencia con resultados Python recuperados: es una comprobación de consistencia interna, no una validación independiente.
- La clasificación empleó referencias GHSL para entrenamiento y su validación independiente sigue pendiente; también debe revisarse la aptitud predictiva del modelo de proyección.
- Para capas web GeoJSON (EPSG:4326), el contorno de la ONE puede generalizarse para mostrarlo en pantalla. Una generalización no debe utilizarse para mediciones, recortes precisos ni decisiones prediales; conserva el GeoPackage original EPSG:32619 como referencia de análisis.

**Procedencia:** procesamiento y conteo en QGIS por el equipo del proyecto (noviembre de 2026); Sentinel-2/Copernicus, GHSL/JRC como referencia, información censal geográfica ONE, modelo exploratorio tipo MOLUSCE.
