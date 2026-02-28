# 1. Diseño de Pipelines: ¿Cómo decidió dividir un pipeline en componentes? ¿Qué criterios usó para definir las dependencias?

La división del pipeline en componentes se decidió siguiendo una arquitectura modular que separa claramente la ingesta, el procesamiento y la entrega final, tal como se muestra en el diagrama donde las fuentes de datos como API, CSV y bases de datos están aisladas de las transformaciones. Los criterios utilizados para definir las dependencias se basaron en la integridad de los datos, estableciendo que la transformación solo puede ocurrir tras una validación exitosa del esquema y que el enriquecimiento depende de un catálogo de productos actualizado. Este enfoque permite que componentes de control como el monitoreo y el logging actúen de forma transversal durante todo el flujo para asegurar la trazabilidad.

# 2. Orquestación vs Ejecución: ¿Cuál es la diferencia entre orquestar un pipeline y ejecutar sus componentes individualmente?

La diferencia entre orquestar un pipeline y ejecutar sus componentes individualmente radica en la gestión centralizada del flujo de trabajo y el manejo de estados de ejecución. Mientras que la ejecución individual simplemente corre un script de validación o procesamiento sin contexto externo, la orquestación utiliza un controlador principal que carga configuraciones, gestiona los identificadores de ejecución y asegura que las dependencias se cumplan antes de avanzar al siguiente paso. Esto permite que el sistema tenga una visión global de la salud del pipeline y pueda reaccionar ante fallos en cualquier etapa del proceso.

# 3. Manejo de Fallos: ¿Qué estrategias implementaría para reintentos automáticos, continuación desde el punto de fallo y notificaciones escalonadas?

Para el manejo de fallos, los reintentos automáticos se pueden implementar dentro de la lógica del orquestador para reejecutar procesos fallidos antes de declarar un error crítico. La continuación desde el punto de fallo se facilita mediante el registro de logs detallados y la generación de reportes intermedios que permiten identificar exactamente dónde se detuvo el flujo. Las notificaciones escalonadas se gestionan a través de canales configurados que envían alertas específicas en caso de fallos críticos, permitiendo una respuesta rápida del equipo de DataOps.

# 4. Monitoreo: ¿Qué métricas monitorearía para evaluar la salud del pipeline?

La salud del pipeline se evalúa monitoreando métricas como el tiempo total de ejecución, el recuento de registros procesados satisfactoriamente y el éxito de las validaciones de calidad. Es fundamental supervisar umbrales técnicos específicos como la completitud de los datos, la frescura de la información en horas y la variación en el recuento de filas entre ejecuciones para detectar degradaciones en la calidad de la fuente.

# 5. Costos: ¿Cómo optimizaría los costos de ejecución en la nube?

La optimización de costos en la nube se fundamenta en la selección de infraestructura proporcional al volumen de datos, utilizando servicios serverless como Azure Functions para cargas moderadas donde solo se paga por el tiempo de ejecución. Para volúmenes masivos de Big Data, se recurre al procesamiento distribuido en Azure Databricks para aprovechar el paralelismo, reduciendo significativamente los tiempos de procesamiento y, por ende, el costo operativo total en comparación con métodos tradicionales.