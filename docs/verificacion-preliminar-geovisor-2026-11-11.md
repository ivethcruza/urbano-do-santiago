# Verificación preliminar del geovisor de expansión urbana — 11 de noviembre de 2026

**Alcance:** rama `revision/avance-one-expansion-2026-11-11` del repositorio personal. La revisión no supone validación técnica de la clasificación, del modelo predictivo o de la zonificación.

## Comprobaciones ejecutadas
- Catálogo `geovisor/layers.json`: siete capas de expansión por período (2018, 2021, 2024, 2027, 2030, 2033 y 2036), todas `en_revision`, con rutas relativas existentes en el repositorio.
- Capa territorial ONE: activada como contorno municipal; contorno referencial OSM desactivado.
- GeoJSON de 100 m: 5.369 polígonos de tipo Polygon y **0 geometrías inválidas** (Shapely sobre el archivo combinado local), clasificados en siete categorías con atributos `anio` y `tipo`.
- Verificación de atributos y conteos: 2018=843; 2021=457; 2024=869; 2027=185; 2030=450; 2033=935; 2036=1.630 polígonos. **Son conteos de polígonos generalizados, no áreas ni píxeles originales.**
- Sintaxis del archivo `web/assets/js/geovisor.js`: evaluación de sintaxis JavaScript sin error.
- Prototipo HTML/SVG **local e independiente del motor MapLibre**: prueba automatizada con Chromium/Playwright del cambio de visibilidad por año y de los botones «Todos», «Clasificados», «Simulados» y «Ninguno»; sin errores JavaScript reportados. Se comprobó la selección individual del año 2027.

## Pruebas que siguen pendientes antes de integrar la PR en main
1. Ejecutar los comandos oficiales del repositorio en la rama de revisión:
   ```bash
   python3 -m pip install -r requirements.txt
   python3 scripts/validate.py --source
   python3 scripts/build_site.py --output site
   python3 scripts/validate.py --site site
   ```
2. Abrir `site/aplicacion/index.html` mediante servidor HTTP local y verificar la carga de MapLibre, la cartografía ONE y las siete capas; comprobar colores, ventanas emergentes, interruptores y errores de red/consola.
3. Confirmar que los datos y las rutas se sirven bien en una vista previa publicada (si se habilita).
4. Revisar rendimiento web, sobreposición visual, créditos de las fuentes y accesibilidad en móviles.
5. Completar contraste independiente GHSL/Sentinel-2, documentación del modelo tipo MOLUSCE y análisis de incertidumbre antes de cualquier uso decisional.

**Limitación de esta revisión:** desde el entorno de pruebas no se pudo descargar una copia ejecutable completa del repositorio (acceso de red restringido). En GitHub no se encontraron ejecuciones de Actions asociadas a la rama al hacer la consulta. Por ello **no se declara aprobado el build oficial ni el visor MapLibre alojado**.

**Precaución geoespacial:** los GeoJSON a 100 m son solo visuales; cálculos de superficies y superposiciones de exposición deben seguir realizándose sobre los rasters originales de 10 m con el límite ONE de análisis.
