# Justificación y Dependencias del Pipeline

## Justificación del Diseño

El pipeline está diseñado bajo principios de **DataOps**, priorizando la modularidad y la observabilidad.

* **Resiliencia:** La validación temprana evita el procesamiento de datos erróneos.
* **Escalabilidad:** Al separar la transformación del enriquecimiento, permitimos que cada etapa crezca de forma independiente.
* **Observabilidad:** Se integra una capa transversal de monitoreo y alertas para garantizar la trazabilidad de los datos en tiempo real.

---

## Dependencias del Pipeline

Para asegurar la integridad del flujo, se definen las siguientes dependencias lógicas:

* **Validación:** Requiere la disponibilidad de las fuentes (API, CSV, DB) y un esquema versionado para su contraste
* **Transformación:** Depende estrictamente de una validación exitosa del esquema de entrada
* **Enriquecimiento:** Requiere que los datos estén transformados y el catálogo de productos actualizado en el sistema
* **Carga (Data Warehouse / Archivos):** Depende de que el proceso de enriquecimiento haya finalizado sin errores
* **Reportes:** Depende de una carga exitosa en el destino final para asegurar la veracidad de la información
* **Monitoreo, Logging y Alertas:** Dependencias globales; se activan desde el inicio del pipeline y reaccionan ante el estado de cada componente
