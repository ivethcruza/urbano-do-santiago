# QA de D05–D06 · Santiago · 11/11/2026

**Estado:** consistencia interna comprobada; interpretación de amenaza y exposición **pendiente de validación técnica**. No publicar la zonificación como normativa.

## Verificaciones realizadas

- Fuente ONE: 222 polígonos válidos en EPSG:32619; área agregada igual al límite disuelto (429,27 km²).
- Campo `OBJECTID`: 222 identificadores únicos. Campo `ENLACE`: 217 identificadores distintos y cinco códigos repetidos en diez registros; no debe utilizarse como clave única para agregación sin depuración. Verificar estabilidad de `OBJECTID` entre versiones.
- Cuatro TIFF de inundación: EPSG:32619, píxel de ~29,7488 m, `NoData=-9999`, clases presentes 1 a 5. **No incluyen diccionario de clases**; metadatos: solo `AREA_OR_POINT=Area`.
- Hashes SHA-256 de los cuatro TIFF coinciden con `D05_D06_metadatos.json`; confirma identidad, no precisión de la amenaza.
- Tabla de exposición: 888 filas (4 escenarios × 222 barrios), sin valores faltantes; en cada escenario los 222 barrios están representados sin duplicar `OBJECTID`.

## Doble cómputo independiente del área etiquetada como inundación

| TIFF | Área dentro del municipio, km² | Suma atribuida a barrios, km² |
|---|---:|---:|
| FLU RC_T100_2020 | 10,341122 | 10,3402 |
| FLU R85_T100_2050 | 10,611929 | 10,6110 |
| PLU RC_T100_2020 | 46,294775 | 46,2939 |
| PLU R85_T100_2050 | 46,447878 | 46,4470 |

La diferencia de aproximadamente 0,0009 km² por escenario equivale a una celda que no quedó asignada a ningún barrio mediante el centro de píxel; documentar esta pérdida de borde y revisar antes de consolidar indicadores finales.

## Pendientes que impiden validar D05–D06

1. Obtener metadatos del proveedor, diccionario 1–5, unidad/modelo/método, e interpretación verificable de RC, R85, T100, 2020 y 2050.
2. Contrastar amenaza con evidencias históricas y autoridades técnicas; valorar incertidumbre espacial y bordes por barrio.
3. Validar independientemente la clasificación urbana 2018–2024 y la simulación exploratoria a 2036.
4. Integrar población compatible por barrio para análisis poblacional; no inferir personas afectadas, pérdidas o daños a partir de la huella urbana.
5. No sumar FLU y PLU: pueden superponerse. La coincidencia espacial de superficies es **exposición**, no una estimación de riesgo ni un mapa normativo.

**Resultado:** apto para revisión interna exploratoria. Publicación de amenazas en el geovisor, pendiente de confirmación de fuentes y clases.
