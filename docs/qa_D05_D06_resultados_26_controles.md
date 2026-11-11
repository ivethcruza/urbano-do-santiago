# Resultado de control de calidad D05–D06

**Estado de datos:** COHERENTE_EXPLORATORIO
**Validación temática:** PENDIENTE — no publicar amenaza como validada.

| Control | Estado | Observación |
|---|---|---|
| Número de filas | PASA | 888 esperadas, 888 observadas |
| Escenarios declarados | PASA | [('FLU', 'R85_T100_2050'), ('FLU', 'RC_T100_2020'), ('PLU', 'R85_T100_2050'), ('PLU', 'RC_T100_2020')] |
| Unidades por escenario FLU:RC_T100_2020 | PASA | 222 filas, 222 ids distintos |
| Unidades por escenario FLU:R85_T100_2050 | PASA | 222 filas, 222 ids distintos |
| Unidades por escenario PLU:RC_T100_2020 | PASA | 222 filas, 222 ids distintos |
| Unidades por escenario PLU:R85_T100_2050 | PASA | 222 filas, 222 ids distintos |
| Consistencia de identificadores entre escenarios | PASA | Se esperan los mismos 222 OBJECTID en los cuatro escenarios |
| ENLACE auditado | PASA | 217 valores distintos, 5 códigos duplicados (NO sirve como llave única) |
| Valores y conteos por fila | PASA | 0 filas inconsistentes; muestra: [] |
| Monotonicidad de exposición 2024→2036 | PASA | 0 registros con 2036 menor que 2024 |
| SHA-256 STG_H_FLU_RC_T100_2020.tif | PASA | Coincide con metadatos versionados |
| SHA-256 STG_H_FLU_R85_T100_2050.tif | PASA | Coincide con metadatos versionados |
| SHA-256 STG_H_PLU_RC_T100_2020.tif | PASA | Coincide con metadatos versionados |
| SHA-256 STG_H_PLU_R85_T100_2050.tif | PASA | Coincide con metadatos versionados |
| Estructura ráster STG_H_FLU_RC_T100_2020.tif | PASA | EPSG:32619, clases [1, 2, 3, 4, 5] |
| Trazabilidad celdas STG_H_FLU_RC_T100_2020.tif | PASA | 1 píxel(es) con centro municipal sin asignar a barrios |
| Suma tabular vs ráster STG_H_FLU_RC_T100_2020.tif | PASA | Diferencia 0.0000018 km² (redondeo máximo tolerado) |
| Estructura ráster STG_H_FLU_R85_T100_2050.tif | PASA | EPSG:32619, clases [1, 2, 3, 4, 5] |
| Trazabilidad celdas STG_H_FLU_R85_T100_2050.tif | PASA | 1 píxel(es) con centro municipal sin asignar a barrios |
| Suma tabular vs ráster STG_H_FLU_R85_T100_2050.tif | PASA | Diferencia 0.0000015 km² (redondeo máximo tolerado) |
| Estructura ráster STG_H_PLU_RC_T100_2020.tif | PASA | EPSG:32619, clases [1, 2, 3, 4, 5] |
| Trazabilidad celdas STG_H_PLU_RC_T100_2020.tif | PASA | 1 píxel(es) con centro municipal sin asignar a barrios |
| Suma tabular vs ráster STG_H_PLU_RC_T100_2020.tif | PASA | Diferencia 0.0000014 km² (redondeo máximo tolerado) |
| Estructura ráster STG_H_PLU_R85_T100_2050.tif | PASA | EPSG:32619, clases [1, 2, 3, 4, 5] |
| Trazabilidad celdas STG_H_PLU_R85_T100_2050.tif | PASA | 1 píxel(es) con centro municipal sin asignar a barrios |
| Suma tabular vs ráster STG_H_PLU_R85_T100_2050.tif | PASA | Diferencia 0.0000009 km² (redondeo máximo tolerado) |

## Bloqueos que impiden cerrar los entregables
- Diccionario oficial de clases 1–5 y unidades de los rásteres de inundación
- Documento de origen, método y revisión técnica de la amenaza
- Interpretación documentada de RC, R85, T100, 2020 y 2050
- Validación de la clasificación urbana observada y el modelo 2036
- Revisión del método de asignación de píxeles en los bordes de barrios
- Validación de identificadores territoriales y trazabilidad ONE

**Precaución:** ninguna clase 1–5 debe interpretarse como profundidad, velocidad, periodo de retorno, peligrosidad alta/baja u otro grado de amenaza sin ficha técnica de fuente.
