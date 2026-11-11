# Avance técnico D01, D05 y D06 · Santiago de los Caballeros

**Fecha de corte:** 11/11/2026  
**Estado:** análisis exploratorio, **no** producto técnico validado ni delimitación normativa del PMOT.

Este avance continúa la **Ficha 06** y el **Plan integral de pendientes**, que definen D01 (inventario), D05 (inundación piloto) y D06 (exposición/pérdidas).

## D01 — Inventario y coherencia territorial

- Inventariados 33 insumos locales disponibles, con huella digital SHA-256, resoluciones y CRS en la matriz de trabajo (archivos conservados fuera del repositorio hasta confirmar derecho de difusión).
- Límite municipal construido de las 31 secciones de la ONE: **429,27 km²**, EPSG:32619.
- `STG_barrios.gpkg`: **222** entidades válidas. El atributo `OBJECTID` tiene 222 identificadores únicos, pero `ENLACE` solo **217** códigos distintos. No usar `ENLACE` como llave única sin depuración.
- Verificación de huella urbana: `huella_2018_2036.tif` recortada hasta 2024 coincide píxel a píxel con `built_2024.tif`.

## D05–D06 — Primer cruce territorial

Los cuatro TIFF categóricos tienen CRS EPSG:32619, tamaño de celda ~29,75 m y clases enteras 1–5. Para esta verificación se usó asignación territorial por centro de píxel, y se calculó la fracción de la huella urbana de 10 m remuestreada a la rejilla de amenaza mediante promedio.

| Tipo de archivo | Código de escenario | Barrios con celdas | Huella categórica (km²) | Huella urbana 2024 coincidente (km²) | Huella urbana simulada 2036 coincidente (km²) |
|---|---|---:|---:|---:|---:|
| Fluvial | RC_T100_2020 | 29 | 10,340 | 1,333 | 2,394 |
| Fluvial | R85_T100_2050 | 30 | 10,611 | 1,372 | 2,462 |
| Pluvial | RC_T100_2020 | 213 | 46,294 | 11,164 | 17,006 |
| Pluvial | R85_T100_2050 | 214 | 46,447 | 11,243 | 17,106 |

Se generaron **888 registros** (222 barrios × cuatro archivos), con códigos de las cinco clases y coincidencia de superficie construida de 2024 y simulada de 2036.

**Advertencias esenciales:**
- Las etiquetas `RC`, `R85` y `T100` son las del nombre de archivo; aún se necesita **fuente/diccionario** que aclare su significado. No asumir periodo de retorno, probabilidad ni nivel de peligro de las clases 1–5.
- Huellas fluviales y pluviales pueden superponerse; **no sumar** directamente.
- La cifra 2036 es una **simulación de expansión urbana** y no una medición.
- Sin GHS-POP/ONE, curvas de daño, inventarios, alturas y valores verificados, **no hay estimaciones validadas de personas expuestas, daño, pérdidas monetarias o pérdida anual esperada**.
- El método de centro de celda tiene incertidumbre de borde; resolución ~30 m. No usar para permisos ni para establecer restricciones PMOT.

## Productos conservados en el paquete de revisión

- Inventario D01 con 33 insumos y hashes, y matriz de 10 grupos de datos pendientes.
- 4 capas GeoPackage para QGIS: `flu_2020`, `flu_2050`, `plu_2020`, `plu_2050` (222 barrios cada una).
- CSV detallado de 888 registros y resumen municipal.
- Informe Word, matriz Excel D01–D09, dos mapas PNG y script reproducible.
- Los datos locales y mapas **no se publican automáticamente** en el geovisor hasta confirmar licencias, procedencia y criterios de aceptación.

## Próximas dependencias

1. **D03**: validación independiente de clasificación y análisis de errores de cambio.
2. **D05**: procedencia de capas y clases; registros hidrológicos y contraste observado; piloto de calibración.
3. **D06**: población/valor económico y vulnerabilidad documentados; sensibilidad por barrio.
4. **D07**: desarrollar matriz técnica orientativa para PMOT; validación con instituciones competentes.
5. **D08/D09**: cargar **solo** capas autorizadas y verificadas al visor, completar manual, actas y transferencia.

**Referencias internas:** `Ficha_06_Republica_Dominicana_Zonificacion_Riesgo_Santiago.docx`; `Plan_Integral_Pendientes_Copernicus_Santiago.docx`; metadatos de los TIFF y GeoPackage utilizados en la corrida local.
