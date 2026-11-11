# Protocolo de validación y criterios de cierre de D05–D06

**Proyecto:** Zonificación del riesgo de desastres orientada al ordenamiento territorial — Santiago de los Caballeros  
**Corte:** 11 de noviembre de 2026  
**Versión:** borrador técnico 0.1, pendiente de aprobación institucional  
**Alcance:** capas de inundación fluvial y pluvial, cruce con 222 barrios/parajes ONE, y huella urbana 2024 / escenario exploratorio 2036.

## 1. Dictamen de avance

Los archivos de cálculo pueden conservarse como **evidencia preliminar de exposición física**. La auditoría automatizada obtuvo 26/26 controles internos satisfactorios; los resultados NO certifican que las magnitudes de amenaza, probabilidades, escenarios ni proyecciones estén validados. El cierre técnico de D05 y D06 permanece condicionado a documentación del origen de las capas y revisión independiente.

Para fines del proyecto:
- **D05 — Amenaza por inundación:** se dispone de cuatro huellas clasificadas en valores 1–5. No se conocen unidades físicas ni definición de clase.
- **D06 — Exposición territorial:** se dispone del cruce espacial de las huellas con la unidad barrio y superficie urbana clasificada para 2024 y simulada para 2036. No se dispone de una estimación validada de población afectada, daños o pérdidas.
- Las etiquetas `RC`, `R85`, `T100`, `2020` y `2050` se conservan literalmente, **sin asumir** su significado técnico.

## 2. Control QA reproducible

**Insumos auditados:** `STG_barrios.gpkg`, `STG_limite_municipal_recuperado.gpkg`, cuatro TIFF `STG_H_FLU/PLU_*.tif`, `D05_D06_inundacion_exposicion_por_barrio.csv`, `D05_D06_metadatos.json`.

**Controles implementados:** presencia de cuatro escenarios; 222 barrios únicos por escenario; 888 registros; mismo conjunto de `OBJECTID`; detección de códigos `ENLACE` repetidos; sumas de clase por fila; superficies no negativas; relaciones lógicas entre inundación y expansión urbana; progresión 2024–2036; SHA-256 de los cuatro TIFF; proyección EPSG:32619; clases de valor 1–5; diferencia espacial municipal/barrial y concordancia con tabla exportada.

### Superficies de inundación, sin interpretación de intensidad

| Archivo | Superficie municipal (km²) | Superficie atribuida a barrios (km²) | Sin asignar (km²) |
|---|---:|---:|---:|
| `STG_H_FLU_RC_T100_2020.tif` | 10.341122 | 10.340237 | 0.000885 |
| `STG_H_FLU_R85_T100_2050.tif` | 10.611929 | 10.611044 | 0.000885 |
| `STG_H_PLU_RC_T100_2020.tif` | 46.294775 | 46.293890 | 0.000885 |
| `STG_H_PLU_R85_T100_2050.tif` | 46.447878 | 46.446993 | 0.000885 |

> Las superficies anteriores se calculan sobre todas las celdas de valores 1–5, pero no prueban que estas celdas correspondan a una inundación para cierto período de retorno o a un umbral físico específico. **No sumar** FLU y PLU debido al posible solapamiento.

## 3. Ficha de verificación de la fuente de amenaza (obligatoria)

Solicitar al productor de las cuatro capas:

1. Institución productora, persona o unidad técnica responsable, contacto institucional y autorización de difusión.
2. Nombre oficial del producto, versión, fecha, cobertura y licencia.
3. Método de modelación, supuestos hidrológicos e hidráulicos o criterios de susceptibilidad utilizados; condiciones de borde y resolución nativa.
4. Significado de cada valor 1, 2, 3, 4 y 5, **incluyendo magnitud, unidad, umbrales y tratamiento de valores NoData**.
5. Definiciones oficiales de `FLU`, `PLU`, `RC`, `R85`, `T100`, `2020` y `2050`, incluyendo si los nombres codifican período de retorno, proyección climática o modelo y los supuestos asociados.
6. Fuente y fecha del DEM, lluvia, drenaje, cauces, usos de suelo y calibración contra eventos observados.
7. Método de validación, métricas reportadas, incertidumbre e idoneidad para planificación municipal.
8. Restricciones de uso y resolución apropiada; condiciones para publicación como datos de amenaza.

**Regla:** no traducir ni clasificar en bajo/medio/alto ni asignar umbrales a los valores 1–5 sin una ficha técnica firmada o una fuente primaria verificable.

## 4. Revisión de la base territorial ONE

- Mantener `OBJECTID` como identificador **de la versión del archivo recibida**, sin asumir que permanecerá igual tras una actualización de la ONE.
- Documentar los 5 códigos `ENLACE` repetidos en 10 entidades; consultar a la ONE si el campo identifica unidades o relaciones y cuál es la llave territorial estable.
- Incorporar fecha, versión y procedencia de la cartografía. Usar geometrias originales EPSG:32619 para cálculos y un contorno generalizado exclusivamente para web.
- Verificar que las 222 entidades estén asociadas a la misma versión municipal y que no existan omisiones o solapamientos significativos.

## 5. Revisión del cruce espacial por celdas

El método actual asigna cada píxel de amenaza a un barrio mediante el **centro de la celda**. Existe una diferencia de una celda en cada escenario entre el total municipal y el total atribuible a barrios, aproximadamente 885 m².

Antes del cierre, comparar al menos dos alternativas:

- **Alternativa A:** identificación y corrección documentada de celdas en límite de barrio mediante criterio de máxima intersección o zona territorial válida.
- **Alternativa B:** intersección de celdas con polígonos barriales para repartir el área proporcionalmente, solo si la precisión requerida y el costo de cálculo lo justifican.

La alternativa seleccionada debe preservar aproximadamente el área municipal total y registrar la incertidumbre por píxel (~29.75 m). No forzar una asignación arbitraria de píxel solamente para obtener cifras iguales.

## 6. Criterios de aceptación para entrega

| Bloque | Evidencia requerida | Estado al corte |
|---|---|---|
| Integridad de insumos | Inventario, rutas, SHA-256 y metadatos | Cumplido para insumos auditados |
| QA tabular/geoespacial | Script, 26 controles y reporte de diferencias | Cumplido, exploratorio |
| Clases de amenaza | Definición física 1–5, unidades y NoData | **Bloqueante: pendiente** |
| Escenarios | Significado y supuestos de códigos de archivo | **Bloqueante: pendiente** |
| Desempeño del modelo | Validación territorial e incertidumbre | **Bloqueante: pendiente** |
| Unidades territoriales | Llave ONE estable y revisión ENLACE | Pendiente |
| Concordancia municipal/barrial | Método definitivo de tratamiento de bordes | Pendiente |
| Uso del suelo | Validación independiente de huella 2024 | Pendiente |
| Proyección de expansión | Validación de escenarios tipo MOLUSCE | Pendiente |
| Entregables finales | Informe firmado, mapas con fuentes, metadatos y geodatos autorizados | Pendiente |

**Cierre D05:** solamente después de verificar metodológicamente las capas de amenaza y documentar sus clases, escenarios y nivel de incertidumbre.  
**Cierre D06:** requiere además un cruce espacial reproducible, criterios territoriales resueltos y definición inequívoca del concepto de exposición. Población afectada y pérdida monetaria son componentes separados que requieren insumos adicionales.

## 7. Productos que pueden entregarse ahora

- Tabla por barrio y escenario con indicadores espaciales identificados como preliminares.
- GeoPackage con cuatro capas temáticas para análisis interno en QGIS.
- Reporte de auditoría de integridad, validación de conteos y brecha de celda en el borde.
- Mapa exploratorio de coincidencia entre huella urbana y huella de inundación, sin simbología de intensidad no documentada.

**Productos que NO deben declararse definitivos todavía:** mapa de riesgo normativo, clasificación de amenaza alta/media/baja, exposición poblacional, pérdidas monetarias, probabilidad anual o daños modelados sobre la base de estas cuatro capas.

## 8. Procedimiento de seguimiento

Usar `Validar_D05_D06_Santiago.py` para repetir la auditoría cada vez que se actualicen los insumos. Registrar fecha y SHA-256 de los cambios; conservar todas las versiones. Completar `Solicitud_Metadatos_Inundacion_Santiago.csv` con evidencia verificable y revisar el dictamen antes de integrar capas de amenaza en el geovisor público.

**Nota adicional:** el archivo independiente `escenarios_inundacion.csv` contiene resultados poblacionales y económicos procedentes de cálculos no trazados en este protocolo; no incorporarlos automáticamente a D06 sin verificar su modelo, fuente, unidades y comparabilidad con los cuatro TIFF analizados.
