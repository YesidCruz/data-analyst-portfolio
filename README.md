PLAN DE APRENDIZAJE

Plan profesional para aprender Análisis de Datos
Ruta práctica de 24 semanas con proyecto guiado de la vida real
Yesid, por tu experiencia en QA/QC eléctrico, instrumentación, control documental, Excel, Power BI y proyectos industriales, no te conviene empezar con ejercicios genéricos de ventas de supermercado. La mejor estrategia es construir un proyecto que conecte tu experiencia técnica con las funciones reales de un Analista de Datos Junior.
El objetivo no será solamente aprender herramientas. Vas a practicar el ciclo completo que se ejecuta en una empresa:

Entender el problema → recopilar datos → limpiar → validar → analizar → visualizar → comunicar → automatizar → documentar.


1. Objetivo general
En 24 semanas desarrollarás un proyecto completo llamado:
Sistema de analítica para el seguimiento QA/QC de proyectos industriales
El sistema permitirá controlar:

Avance programado y ejecutado.
Curva S.
Actividades QA/QC.
Inspecciones.
Equipos y suministros.
Dossiers.
Punch list.
No conformidades — NCR.
Documentos pendientes.
Certificados de conformidad.
Desempeño por proyecto, contratista, disciplina y responsable.
Riesgos de atraso.
Indicadores gerenciales.
Calidad de la información.

Este proyecto podrá formar parte de tu:

Portafolio profesional.
GitHub.
LinkedIn.
Hoja de vida.
Entrevistas para cargos de analista.
Presentación interna ante Bureau Veritas o Ecopetrol, utilizando información ficticia o anonimizada.


2. Resultado esperado al terminar
Al finalizar tendrás:

Un archivo de datos original o Raw Data.
Un conjunto de datos limpio.
Un diccionario de datos.
Un documento de requerimientos.
Consultas SQL.
Un análisis exploratorio en Python.
Un dashboard profesional en Power BI.
Un informe ejecutivo.
Un repositorio organizado en GitHub.
Una presentación tipo caso de estudio.
Un portafolio que demuestre el proceso completo.
Experiencia práctica para explicar el proyecto en una entrevista.


3. Herramientas que utilizarás
Herramientas principales

Excel: captura, exploración inicial, tablas y validaciones.
Power Query: limpieza y transformación.
SQL: consulta y análisis de bases de datos.
Power BI: modelo, DAX, visualización y storytelling.
Python: análisis exploratorio, validación y automatización.
GitHub: documentación y portafolio.
Microsoft Word o Markdown: informe y documentación.
PowerPoint: presentación ejecutiva final.

Herramientas opcionales

SharePoint Lists.
Power Automate.
Microsoft Forms.
Power Apps.
GitHub Codespaces.
Google Colab.

No necesitas dominar todo al principio. La ruta está organizada para sumar herramientas gradualmente.

4. Dedicación recomendada
Plan estándar

Lunes a jueves: 60 a 75 minutos diarios.
Sábado: 2 a 3 horas de proyecto.
Total: 6 a 8 horas por semana.

Distribución semanal

20 % teoría.
30 % ejercicios.
40 % proyecto.
10 % documentación y reflexión.

La regla principal será:

Cada semana debes producir una evidencia verificable, no solamente ver cursos o videos.


5. Escenario del proyecto
Trabajarás como un Analista de Datos Junior asignado a una oficina de proyectos industriales.
La gerencia indica:

“Actualmente tenemos información dispersa en archivos Excel. No podemos identificar con rapidez cuáles proyectos están atrasados, cuántas inspecciones están pendientes, qué contratistas tienen más no conformidades ni cuál es el estado real de los dossiers. Necesitamos una solución confiable para hacer seguimiento y tomar decisiones.”

Tu responsabilidad será transformar esa solicitud en un producto analítico.

6. Estructura de datos del proyecto
Construirás progresivamente las siguientes tablas.
Tabla de proyectos

ID_Proyecto
Nombre_Proyecto
Gerencia
Contratista
Fecha_Inicio
Fecha_Fin_Planeada
Fecha_Fin_Real
Presupuesto
Estado
Responsable

Tabla de actividades

ID_Actividad
ID_Proyecto
Capítulo
Subcapítulo
Actividad
Disciplina
Responsable
Fecha_Programada
Fecha_Ejecutada
Programado
Ejecutado
Peso
Estado

Tabla de inspecciones

ID_Inspeccion
ID_Proyecto
Tipo_Inspeccion
Equipo
Proveedor
Fecha_Programada
Fecha_Real
Resultado
Inspector
Observaciones

Tabla de NCR

ID_NCR
ID_Proyecto
Contratista
Especialidad
Fecha_Apertura
Fecha_Compromiso
Fecha_Cierre
Criticidad
Estado
Causa
Responsable

Tabla de punch list

ID_Punch
ID_Proyecto
Sistema
Subsistema
Categoría
Fecha_Apertura
Fecha_Compromiso
Fecha_Cierre
Estado
Responsable

Tabla documental

ID_Documento
ID_Proyecto
Tipo_Documento
Código_Documento
Revisión
Fecha_Programada
Fecha_Recibida
Estado
Responsable
Días_Atraso

Tabla calendario

Fecha
Año
Mes
Número_Mes
Trimestre
Semana
Año_Semana
Día
Es_Laborable


7. Ruta detallada semana por semana

FASE 1 — Fundamentos y comprensión del negocio
Semana 1 — Rol del analista y definición del problema
Objetivo
Comprender qué hace un analista y convertir una necesidad del negocio en preguntas analíticas.
Contenido

Diferencia entre dato, información e indicador.
Funciones del analista junior.
Ciclo de vida del análisis.
Tipos de análisis:

Descriptivo: ¿qué pasó?
Diagnóstico: ¿por qué pasó?
Predictivo: ¿qué podría pasar?
Prescriptivo: ¿qué deberíamos hacer?


Interesados o stakeholders.
Requerimientos funcionales.

Actividad guiada
Redactar el problema del proyecto:

La organización no cuenta con una fuente consolidada para controlar el avance QA/QC y necesita identificar atrasos, pendientes, desviaciones y responsables.

Preguntas de negocio
Debes crear al menos 15. Ejemplos:

¿Cuál es el avance global de cada proyecto?
¿Cuál es la diferencia entre avance programado y ejecutado?
¿Qué proyecto presenta la mayor desviación?
¿Cuántas NCR se encuentran abiertas?
¿Cuántas NCR están vencidas?
¿Qué contratista genera más no conformidades?
¿Cuál es el tiempo promedio de cierre?
¿Cuántas inspecciones fueron rechazadas?
¿Qué documentos están vencidos?
¿Qué responsable concentra más pendientes?

Entregable
Documento:
Plain Text101_Requerimientos_Proyecto.mdMostrar más líneas
Debe incluir:

Antecedentes.
Problema.
Objetivo general.
Objetivos específicos.
Alcance.
Exclusiones.
Interesados.
Preguntas del negocio.
Indicadores preliminares.

Evidencia profesional
Simular una reunión de levantamiento de requerimientos y escribir una minuta.

Semana 2 — Fundamentos de Excel para análisis
Objetivo
Organizar datos correctamente antes de analizarlos.
Contenido

Filas, columnas y registros.
Tablas estructuradas.
Tipos de datos.
Referencias relativas y absolutas.
Ordenamiento.
Filtros.
Formato condicional.
Validación de datos.
Eliminación de duplicados.
Funciones básicas:

SUMA
PROMEDIO
CONTAR
CONTARA
CONTAR.SI
SUMAR.SI
SI
SI.ERROR



Actividad guiada
Crear la tabla inicial de actividades QA/QC con mínimo 100 registros.
Reglas

Una fila representa una actividad.
Una columna representa una variable.
No combinar celdas.
No insertar subtotales dentro de la tabla.
No utilizar colores como dato.
No incluir múltiples valores en una misma celda.
Mantener identificadores únicos.

Entregable
Plain Text102_Base_Actividades_QAQC.xlsxMostrar más líneas
Control de calidad
Comprobar:

¿Existen IDs duplicados?
¿Las fechas son fechas reales?
¿Programado y Ejecutado son numéricos?
¿Los estados tienen nombres consistentes?
¿Existen campos obligatorios vacíos?


Semana 3 — Fórmulas y lógica de indicadores
Objetivo
Construir indicadores básicos usando reglas claras.
Contenido

BUSCARX
INDICE y COINCIDIR
CONTAR.SI.CONJUNTO
SUMAR.SI.CONJUNTO
Funciones de fecha.
Funciones de texto.
Manejo de errores.
Cálculo de porcentajes.
Indicadores y reglas de negocio.

Indicadores para construir

Avance de actividad.
Cumplimiento.
Diferencia programado-ejecutado.
Días de atraso.
Estado de plazo.
Semáforo.
Actividades pendientes.
Actividades vencidas.

Regla recomendada para avance
Si Programado y Ejecutado son cantidades:
Excel1=SI.ERROR(MIN([@Ejecutado]/[@Programado];1);0)2`Mostrar más líneas
El uso de MIN evita mostrar avances superiores al 100 %, si esa es la regla aprobada.
Entregable
Archivo actualizado con:

Hoja Datos.
Hoja Parámetros.
Hoja Validaciones.
Hoja Indicadores.
Hoja Resumen.

Evidencia profesional
Crear una sección llamada Reglas de negocio, explicando cómo se calcula cada KPI.

Semana 4 — Tablas dinámicas y análisis descriptivo
Objetivo
Responder preguntas del negocio mediante agrupaciones.
Contenido

Tablas dinámicas.
Campos calculados.
Segmentadores.
Línea de tiempo.
Agrupación por meses.
Distribución.
Frecuencia.
Tendencia.
Comparación.
Participación porcentual.

Análisis requerido

Actividades por proyecto.
Actividades por estado.
Cumplimiento por responsable.
Avance por capítulo.
Actividades vencidas por contratista.
Evolución semanal.
Pareto de causas de atraso.

Entregable
Dashboard preliminar en Excel con:

4 tarjetas KPI.
3 gráficos.
2 segmentadores.
1 tabla de detalle.

Revisión de fin de fase
Debes ser capaz de explicar:

Qué problema estás resolviendo.
Qué representa cada fila.
Qué significa cada KPI.
Qué decisiones permite tomar el resumen.


FASE 2 — Preparación y calidad de datos
Semana 5 — Calidad de datos
Objetivo
Aprender a detectar errores antes de producir resultados.
Dimensiones de calidad

Completitud.
Unicidad.
Validez.
Consistencia.
Exactitud.
Oportunidad.
Integridad.

Actividad guiada
Crear una tabla de auditoría:








































ReglaCampoError detectadoSeveridadAcciónID únicoID_ActividadID repetidoAltaEliminar o reconstruirFecha válidaFecha_EjecutadaFecha anterior al inicioAltaRevisar fuenteEstado permitidoEstado“Termiando”MediaEstandarizarCampo obligatorioResponsableValor vacíoMediaSolicitar corrección
Entregable

Meta
Crear al menos:

10 reglas de calidad.
5 controles automáticos.
1 indicador de calidad global.


Semana 6 — Power Query: importar y limpiar
Objetivo
Reemplazar pasos manuales por transformaciones repetibles.
Contenido

Importar Excel y CSV.
Tipos de datos.
Eliminar columnas.
Reemplazar valores.
Quitar espacios.
Dividir y combinar columnas.
Agregar columnas.
Anexar consultas.
Combinar tablas.
Parámetros.
Actualización.

Actividad guiada
Crear tres archivos mensuales:
Plain Text1Actividades_Mayo.xlsx2Actividades_Junio.xlsx3Actividades_Julio.xlsxMostrar más líneas
Power Query deberá:

Leer todos los archivos desde una carpeta.
Consolidarlos.
Estandarizar campos.
eliminar duplicados.
Ajustar tipos.
Crear columnas de control.
cargar el resultado.

Entregable
Plain Text104_ETL_Actividades_QAQC.xlsx2``Mostrar más líneas
Evidencia profesional
Documentar cada transformación:

Problema encontrado.
Paso aplicado.
Motivo.
Impacto.


Semana 7 — Modelo relacional
Objetivo
Dejar de trabajar con una sola tabla gigante.
Contenido

Tabla de hechos.
Dimensiones.
Claves primarias.
Claves foráneas.
Relaciones.
Cardinalidad.
Esquema estrella.
Integridad referencial.
Granularidad.

Modelo sugerido
Tabla de hechos:

Fact_Actividades
Fact_Inspecciones
Fact_NCR
Fact_Documentos

Dimensiones:

Dim_Proyecto
Dim_Responsable
Dim_Contratista
Dim_Estado
Dim_Calendario

Actividad guiada
Dibujar el modelo e identificar:

Qué representa cada fila.
Cuál es la llave de cada tabla.
Cómo se relacionan las tablas.
Qué campos deben separarse como dimensiones.

Entregable
Plain Text105_Modelo_Datos.png205_Diccionario_Datos.xlsxMostrar más líneas

Semana 8 — Estadística descriptiva
Objetivo
Interpretar correctamente los datos.
Contenido

Media.
Mediana.
Moda.
Mínimo y máximo.
Rango.
Percentiles.
Varianza.
Desviación estándar.
Valores atípicos.
Sesgos.
Correlación, sin asumir causalidad.

Aplicación al proyecto
Calcular:

Promedio de días de cierre de NCR.
Mediana de días de atraso.
Percentil 75 de tiempo de respuesta.
Contratistas con mayor variabilidad.
Valores atípicos en cierre de documentos.
Distribución de inspecciones por resultado.

Entregable
Plain Text106_Analisis_Estadistico.xlsxMostrar más líneas
Revisión de fin de fase
Presentar cinco hallazgos con esta estructura:

Hallazgo.
Evidencia.
Impacto.
Posible causa.
Recomendación.


FASE 3 — SQL para analistas
Semana 9 — Fundamentos de SQL
Objetivo
Consultar información utilizando sentencias básicas.
Contenido

Base de datos.
Tabla y registro.
SELECT
FROM
WHERE
ORDER BY
DISTINCT
LIMIT
Alias.
Operadores lógicos.

Consultas esperadas

Actividades abiertas.
Actividades vencidas.
Proyectos activos.
NCR críticas.
Documentos pendientes.
Inspecciones rechazadas.

Entregable
Plain Text1sql/01_consultas_basicas.sqlMostrar más líneas
Cada consulta debe contener:
SQL1-- Objetivo:2-- Pregunta de negocio:3-- Resultado esperado:Mostrar más líneas

Semana 10 — Agregaciones SQL
Contenido

COUNT
SUM
AVG
MIN
MAX
GROUP BY
HAVING
CASE WHEN

Reto
Construir consultas para:

NCR por proyecto.
Días promedio de cierre.
Cumplimiento por contratista.
Inspecciones aprobadas y rechazadas.
Clasificación por semáforo.
Top cinco responsables con mayores pendientes.

Entregable


Semana 11 — Uniones y fechas en SQL
Contenido

INNER JOIN
LEFT JOIN
Diferencia entre WHERE y HAVING.
Campos nulos.
Funciones de fecha.
Diferencias entre fechas.
Subconsultas.

Actividad
Relacionar:

Proyectos con actividades.
Proyectos con NCR.
Contratistas con inspecciones.
Responsables con documentos.
Calendario con actividades.

Entregable
Plain Text1sql/03_joins_y_fechas.sqlMostrar más líneas
Error profesional que debes aprender a evitar
Un JOIN mal construido puede duplicar registros y producir KPIs falsos. Siempre compara:

Cantidad antes del JOIN.
Cantidad después del JOIN.
Número de IDs únicos.
Sumas antes y después.


Semana 12 — SQL aplicado al negocio
Objetivo
Construir una consulta consolidada para alimentar el dashboard.
Actividad principal
Crear una vista analítica con:

Proyecto.
Contratista.
Responsable.
Fecha.
Programado.
Ejecutado.
Avance.
Desviación.
Pendientes.
Vencidos.
Semáforo.

Reto adicional
Crear una consulta que clasifique proyectos:

Verde: desviación menor o igual a 5 %.
Amarillo: desviación mayor a 5 % y menor o igual a 10 %.
Rojo: desviación superior a 10 %.

Entregable
Plain Text1sql/04_vista_analitica_proyectos.sqlMostrar más líneas
Revisión de fase
Debes resolver diez preguntas de negocio usando solamente SQL.

FASE 4 — Power BI profesional
Semana 13 — Importación y Power Query en Power BI
Objetivo
Construir el archivo base del dashboard.
Contenido

Obtener datos.
Consultas de preparación.
Referenciar consultas.
Deshabilitar carga.
Parámetros.
Carpetas.
Convenciones de nombres.
Perfilado de columnas.

Convención
Plain Text1stg_Actividades2stg_Proyectos3stg_NCR4dim_Proyecto5dim_Calendario6fact_Actividades7fact_NCRMostrar más líneas
stg significa tabla de preparación o staging.
Entregable
Plain Text107_Dashboard_QAQC.pbixMostrar más líneas

Semana 14 — Modelado en Power BI
Contenido

Esquema estrella.
Relaciones uno a muchos.
Dirección del filtro.
Tabla calendario.
Tabla de medidas.
Ocultar campos técnicos.
Jerarquías.
Ordenar columnas.

Actividad guiada
Construir:

Dim_Calendario.
Dim_Proyecto.
Dim_Responsable.
Dim_Contratista.
Fact_Actividades.
Fact_NCR.

Control
Evitar:

Relaciones muchos a muchos innecesarias.
Relaciones bidireccionales sin justificación.
Medidas almacenadas en tablas aleatorias.
Uso excesivo de columnas calculadas.


Semana 15 — DAX básico
Contenido

Medidas frente a columnas calculadas.
Contexto de filtro.
SUM
COUNTROWS
DISTINCTCOUNT
DIVIDE
CALCULATE
Variables con VAR.
Manejo de valores vacíos.

Medidas mínimas
DAX1Total Actividades =2COUNTROWS(Fact_Actividades)Mostrar más líneas
DAX1Actividades Ejecutadas =2CALCULATE(3    COUNTROWS(Fact_Actividades),4    Fact_Actividades[Estado] = "Ejecutada"5)Mostrar más líneas

DAX1Desviación =2[Avance Ejecutado %] - [Avance Programado %]Mostrar más líneas
Entregable
Crear por lo menos 15 medidas documentadas.

Semana 16 — Inteligencia de tiempo y Curva S
Objetivo
Comparar avance planificado y real a través del tiempo.
Contenido

Acumulados.
Fecha máxima.
Contexto temporal.
Semana ordenada.
Año-semana.
Programado acumulado.
Ejecutado acumulado.
Desviación acumulada.

Visual principal
Curva S con:

Eje X: Año-Semana.
Línea 1: Programado acumulado.
Línea 2: Ejecutado acumulado.
Línea 3 opcional: Proyección.

Controles fundamentales

La semana debe ordenarse por una columna numérica.
No sumar porcentajes directamente.
Verificar que el acumulado no disminuya.
Confirmar que el último punto coincida con el total.
Revisar filtros de proyecto y año.

Entregable
Página Avance y Curva S.

Semana 17 — Diseño del dashboard
Objetivo
Transformar cálculos en una interfaz ejecutiva.
Página 1 — Resumen ejecutivo

Avance programado.
Avance ejecutado.
Desviación.
Actividades vencidas.
NCR abiertas.
Documentos pendientes.
Curva S.
Estado por proyecto.
Principales alertas.

Página 2 — Actividades

Estado de actividades.
Avance por capítulo.
Cumplimiento por responsable.
Tabla detallada.
Atrasos.

Página 3 — NCR y punch list

NCR abiertas y cerradas.
NCR vencidas.
Tiempo medio de cierre.
Pareto de causas.
Tendencia mensual.
Detalle crítico.

Página 4 — Inspecciones y documentación

Inspecciones por resultado.
Certificados pendientes.
Documentos vencidos.
Desempeño del proveedor.
Próximos compromisos.

Página 5 — Calidad de datos

Registros incompletos.
Duplicados.
Fechas inválidas.
Última actualización.
Porcentaje de calidad.

Entregable
Primera versión funcional del dashboard.

Semana 18 — Storytelling e insights
Objetivo
Evitar que el dashboard sea solamente una colección de gráficos.
Estructura para cada insight

Qué ocurrió → dónde ocurrió → por qué importa → qué se recomienda.

Ejemplo

El proyecto Alfa presenta una desviación de -12 %, concentrada principalmente en actividades documentales y cierre de punch list. El 63 % de los pendientes corresponde al contratista X. Se recomienda priorizar los 15 elementos críticos vencidos y establecer seguimiento dos veces por semana.

Actividad
Redactar:

5 hallazgos.
5 riesgos.
5 recomendaciones.
3 decisiones sugeridas.
1 conclusión ejecutiva.

Entregable
Página Hallazgos y recomendaciones.

FASE 5 — Python para análisis
Semana 19 — Fundamentos de Python
Objetivo
Utilizar Python como herramienta complementaria.
Contenido

Variables.
Listas.
Diccionarios.
Condicionales.
Ciclos.
Funciones.
Importación de librerías.
Lectura de archivos.

Entorno recomendado

Google Colab o GitHub Codespaces.
Python.
Pandas.
Matplotlib.

Primer ejercicio
Python1import pandas as pd2 3df = pd.read_excel("Base_Actividades_QAQC.xlsx")4 5print(df.head())6print(df.shape)7print(df.info())Mostrar más líneas
Entregable


Semana 20 — Limpieza de datos con Pandas
Contenido

Valores nulos.
Duplicados.
Tipos de datos.
Fechas.
Texto.
Filtros.
Columnas calculadas.
Agrupaciones.

Flujo esperado
Python1import pandas as pd2 3df = pd.read_excel("Base_Actividades_QAQC.xlsx")4 5df.columns = df.columns.str.strip()6df = df.drop_duplicates(subset=["ID_Actividad"])7 8df["Fecha_Programada"] = pd.to_datetime(9    df["Fecha_Programada"],10    errors="coerce"11)12 13df["Responsable"] = df["Responsable"].str.strip().str.title()Mostrar más líneas
Entregable


Semana 21 — Análisis exploratorio
Objetivo
Encontrar patrones que no sean evidentes a simple vista.
Análisis requerido

Distribución de estados.
Atrasos por contratista.
Tendencia semanal.
Tiempo de cierre.
Outliers.
Correlaciones válidas.
Valores faltantes.
Concentración de pendientes.
Pareto.
Comparación entre proyectos.

Entregable

El notebook debe contener:

Pregunta.
Código.
Resultado.
Interpretación.
Limitaciones.
Recomendación.


Semana 22 — Automatización y exportación
Objetivo
Crear un proceso repetible.
Actividad
Desarrollar un script que:

Lea los archivos de entrada.
Evalúe calidad.
Limpie los registros.
Calcule indicadores.
Genere tablas resumen.
Exporte resultados.
Registre errores.

Estructura

Entregable
Plain Text1src/pipeline_analitico.py2output/resumen_gerencial.xlsxMostrar más líneas
Nivel junior esperado
No necesitas construir un sistema complejo. Debes demostrar que:

Entiendes la secuencia.
Puedes dividir el problema.
Validaste los resultados.
El proceso puede repetirse.


FASE 6 — Portafolio, entrega y simulación laboral
Semana 23 — GitHub y documentación
Objetivo
Presentar el proyecto como un producto profesional.
Estructura recomendada

README mínimo

Contexto.
Problema.
Objetivo.
Fuente de datos.
Herramientas.
Metodología.
Modelo.
Indicadores.
Capturas.
Hallazgos.
Recomendaciones.
Cómo ejecutar.
Limitaciones.
Próximas mejoras.

Seguridad
No debes publicar:

Nombres reales de proyectos.
Información contractual reservada.
Rutas corporativas.
Correos.
Nombres de trabajadores.
Valores financieros confidenciales.
Documentos de Ecopetrol o Bureau Veritas.
Información técnica restringida.

Utiliza datos ficticios, anonimizados o creados especialmente para el portafolio.

Semana 24 — Presentación final y simulación de entrevista
Objetivo
Defender el proyecto como lo haría un analista junior.
Presentación de 10 minutos

Contexto.
Problema.
Requerimientos.
Fuentes de información.
Problemas de calidad.
Proceso de limpieza.
Modelo.
Dashboard.
Hallazgos.
Recomendaciones.
Limitaciones.
Próximos pasos.

Preguntas de entrevista que debes responder

¿Cuál era el problema del negocio?
¿Cómo comprobó la calidad de los datos?
¿Por qué utilizó un esquema estrella?
¿Cuál fue el error más difícil?
¿Cómo validó sus medidas?
¿Qué diferencia existe entre una medida y una columna?
¿Por qué no se deben sumar porcentajes?
¿Qué hallazgo tuvo mayor impacto?
¿Qué haría si recibe datos incompletos?
¿Cómo evitaría duplicaciones en un JOIN?
¿Cómo aseguraría la actualización?
¿Qué mejoraría en una segunda versión?

Entregable final

Repositorio de GitHub.
Dashboard.
Informe ejecutivo.
Presentación.
Video demostrativo de 3 a 5 minutos.
Publicación profesional para LinkedIn.


8. Rutina exacta para cada semana
Día 1 — Aprendizaje

Estudiar el concepto.
Escribir definiciones con tus propias palabras.
Crear tres ejemplos relacionados con QA/QC.

Día 2 — Práctica controlada

Resolver ejercicios cortos.
Repetir sin copiar.
Registrar errores.

Día 3 — Aplicación

Llevar el concepto al proyecto.
Comparar el resultado con Excel o cálculo manual.
Guardar evidencia.

Día 4 — Validación

Buscar duplicados.
Revisar totales.
Confirmar filtros.
Probar casos extremos.
Documentar supuestos.

Día 5 o sábado — Entrega semanal

Organizar archivos.
Actualizar GitHub.
Escribir conclusiones.
Tomar una captura.
Preparar una explicación de dos minutos.


9. Método de validación profesional
Para cada indicador aplica esta lista:
Validación técnica

¿La fórmula produce errores?
¿El tipo de dato es correcto?
¿Responde adecuadamente a los filtros?
¿Existen valores nulos?
¿Hay divisiones por cero?
¿Los acumulados son coherentes?

Validación de negocio

¿Qué significa el indicador?
¿Quién lo utilizará?
¿Con qué frecuencia?
¿Cuál es la fuente?
¿Cuál es su regla?
¿Cuál es su meta?
¿Qué acción genera?

Validación cruzada
Debes comparar el resultado en al menos dos medios:

Excel frente a Power BI.
SQL frente a Power BI.
Python frente a Excel.
Conteo manual de una muestra.

Ejemplo:
Plain Text1Total esperado manualmente: 1252Resultado en Excel: 1253Resultado en SQL: 1254Resultado en Power BI: 1255Estado: ValidadoMostrar más líneas

10. Sistema de evaluación
Cada semana te puedes calificar sobre 100 puntos:

Comprensión del negocio: 20 puntos.
Preparación de datos: 20 puntos.
Cálculos y análisis: 20 puntos.
Validación: 15 puntos.
Visualización: 10 puntos.
Documentación: 10 puntos.
Comunicación: 5 puntos.

Interpretación

90–100: excelente.
80–89: competente.
70–79: aceptable, requiere ajustes.
Menos de 70: repetir los elementos débiles.

No avances solamente porque acabó la semana. Avanza cuando el entregable sea reproducible y puedas explicarlo.

11. Indicadores finales del proyecto
Como mínimo, el dashboard debe manejar:
Avance

Avance programado.
Avance ejecutado.
Desviación.
Cumplimiento.
Actividades vencidas.
Actividades próximas a vencer.

NCR

NCR totales.
NCR abiertas.
NCR vencidas.
NCR críticas.
Tiempo promedio de cierre.
Porcentaje de cierre.
Pareto de causas.

Inspecciones

Inspecciones programadas.
Inspecciones realizadas.
Inspecciones aprobadas.
Inspecciones rechazadas.
Cumplimiento del plan.
Desempeño por proveedor.

Documentación

Documentos programados.
Documentos recibidos.
Documentos pendientes.
Documentos vencidos.
Tiempo promedio de entrega.
Cumplimiento documental.

Calidad de datos

Registros completos.
Registros duplicados.
Campos inválidos.
Fecha de actualización.
Índice de calidad.


12. Lo que debes poder hacer como analista junior
Al finalizar deberás poder:

Entender una solicitud poco clara.
Formular preguntas al usuario del informe.
Identificar las fuentes de datos.
Construir un diccionario.
Limpiar datos.
Detectar duplicados.
Modelar tablas.
Consultar con SQL.
Crear medidas DAX.
Diseñar un dashboard.
Interpretar indicadores.
Identificar riesgos.
Comunicar hallazgos.
Documentar supuestos.
Presentar recomendaciones.
Reconocer las limitaciones de tu análisis.


13. Primer sprint: tareas para comenzar ahora
Semana 1 — Lista exacta de trabajo
Tarea 1
Crear una carpeta:
Plain Text1Proyecto_Analitica_QAQCMostrar más líneas
Tarea 2
Crear esta estructura:
Plain Text101_Requerimientos202_Datos_Raw303_Datos_Procesados404_Excel505_SQL606_Python707_PowerBI808_Informes909_Presentacion1010_EvidenciasMostrar más líneas
Tarea 3
Crear el documento de requerimientos con:

Nombre del proyecto.
Antecedentes.
Problema.
Objetivo.
Alcance.
Usuarios.
Fuentes.
Indicadores.
Preguntas.
Riesgos.
Supuestos.

Tarea 4
Escribir 15 preguntas del negocio.
Tarea 5
Seleccionar los primeros 10 KPI.
Tarea 6
Definir para cada KPI:
Plain Text1Nombre:2Objetivo:3Fórmula:4Fuente:5Frecuencia:6Responsable:7Meta:8Interpretación:Mostrar más líneas
Tarea 7
Grabar una explicación personal de dos minutos:

“El problema que quiero solucionar es…, los usuarios serán…, las fuentes serán…, y las decisiones que permitirá tomar son…”

Esto mejorará tu comunicación para entrevistas y presentaciones.

14. Recomendación personalizada
En tu caso, la ruta profesional más valiosa sería:

Analista de Datos QA/QC → Analista Power BI → Analista de Calidad de Datos → QA Data Analyst / BI Analyst industrial.

Tu experiencia en ingeniería eléctrica, QA/QC, documentación técnica, inspecciones y proyectos industriales te da una ventaja importante: ya entiendes el negocio. Muchos aspirantes saben crear gráficos, pero no saben interpretar una NCR, un dossier, una inspección, un certificado o un atraso contractual.
Tu objetivo no debe ser competir únicamente como “persona que sabe Power BI”. Debes posicionarte como:

Ingeniero QA/QC especializado en analítica, automatización y visualización de datos para proyectos industriales.

Ese perfil es más diferenciado, creíble y alineado con tu experiencia real.
