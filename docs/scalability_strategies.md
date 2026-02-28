# Estrategias de Escalabilidad

La primera estrategia de escalabilidad se centra en el procesamiento local diseñado para volúmenes de datos inferiores a 1GB. En este nivel inicial, la arquitectura utiliza herramientas estándar como Pandas y Python puro para realizar las tareas de transformación y validación. La ejecución técnica se apoya en runners de GitHub Actions estándar, lo que permite mantener una infraestructura simplificada para cargas de trabajo pequeñas

Cuando la demanda de datos aumenta y se sitúa en un rango de entre 1GB y 10GB, el sistema escala hacia un modelo de procesamiento en la nube utilizando Azure. Para este nivel intermedio, se implementan servicios como Azure Functions y Azure Batch que permiten desacoplar los procesos, Las ventajas operativas más importantes de esta transición incluyen la capacidad de escalado automático y la optimización financiera mediante un esquema de costo por uso

Para el manejo de conjuntos de datos masivos que superan los 10GB, la estrategia evoluciona hacia un entorno de procesamiento distribuido. En esta etapa se integran herramientas de alto rendimiento como Azure Databricks y Azure Synapse para gestionar la carga este enfoque garantiza un procesamiento paralelo eficiente y una arquitectura optimizada específicamente para los retos que presenta el Big Data
