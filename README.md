# Business Performance & Data Pipeline Automation - Supermarket Case Study

## Resumen Ejecutivo
Este proyecto final desarrolla un **Data Pipeline integral (End-to-End)** enfocado en la analítica comercial y financiera de una cadena de supermercados. El objetivo principal es transformar datos transaccionales puros en activos de decisión estratégica para la alta gerencia (C-Suite), demostrando competencias avanzadas en **Arquitectura de Datos (SQL)**, **Análisis Estadístico y Automatización (Python)**, y **Visualización de Negocio (Power BI y Excel)**.

A través de este ecosistema multi-herramienta, se delegó el procesamiento pesado al servidor de base de datos, se automatizó la generación de reportes recurrentes y se extrajeron hallazgos ocultos mediante estadística correlacional.

---

## Insights Críticos de Negocio

Tras consolidar el análisis a lo largo de las diferentes plataformas, se detectaron tres hallazgos clave de alto impacto financiero y operacional:

1. **La Desconexión de la Satisfacción (Insight Estadístico - Python):**
   El análisis de correlación de Pearson demostró que la variable "Calificación" (satisfacción del cliente) tiene una relación prácticamente nula (-0.01 a -0.04) con el ticket de gasto y el volumen de compra. **Traducción de negocio:** Los clientes altamente satisfechos y los insatisfechos gastan exactamente lo mismo por visita en este momento. Esto sugiere que la compra está impulsada por necesidad o cercanía, indicando que las estrategias de fidelización actuales no impactan en el corto plazo y abriendo paso a una auditoría sobre la retención a largo plazo.

2. **La Tarde como Motor Operacional (Análisis Temporal - Power BI/Excel):**
   La franja horaria de la Tarde concentra el mayor volumen operativo, acumulando más de la mitad de la ganancia total generada (`8,213.16`), duplicando el rendimiento de la Noche (`4,223.90`) y triplicando el de la Mañana (`2,412.99`). **Traducción de negocio:** La asignación de personal, reposición de inventario en góndolas y apertura de cajas registradoras deben optimizarse críticamente para el bloque de la tarde para evitar cuellos de botella y pérdidas de ventas potenciales por fricción.

3. **Elasticidad e Inflexibilidad del Margen (Estructura Financiera):**
   El análisis financiero reveló que el margen real de contribución está estancado institucionalmente en un `4.76%` en todas las categorías de productos debido a una indexación fija de costos. **Traducción de negocio:** Dado que el beneficio porcentual por producto es inflexible, el crecimiento de los ingresos depende estrictamente del **volumen de unidades vendidas**. Las campañas de marketing no deben empujar productos individuales de lujo, sino enfocarse en estrategias de Cross-selling (venta cruzada) y promociones por volumen (ej. 3x2) para aumentar la cantidad de artículos por carrito.

---

## Arquitectura del Ecosistema Técnico

El proyecto está diseñado bajo buenas prácticas de ingeniería de datos, estructurado en las siguientes fases replicables:

*   **Fase 1 - SQL (PostgreSQL):** Modelado e ingesta del set de datos transaccional. Creación de 4 vistas de negocio indexadas para centralizar las lógicas de agregación de rentabilidad, franjas horarias, tickets promedio y comportamiento temporal, liberando de carga a las herramientas de reporte.
*   **Fase 2 - Python (Data Science & ETL):** 
    *   `analisis_correlacion.py`: Conexión nativa a PostgreSQL mediante `psycopg2` para procesar matrices estadísticas con `pandas` y exportar mapas de calor visuales con `seaborn`.
    *   `automatizacion_excel.py`: Pipeline automatizado que extrae las vistas SQL directamente del servidor y genera un archivo unificado `.xlsx` estructurado por pestañas utilizando `openpyxl`.
*   **Fase 3 - Power BI Desktop:** Conexión interactiva a las vistas de PostgreSQL en modo *Import*. Aplicación de modelado avanzado (indexación cronológica de días de la semana) y diseño de interfaz ejecutiva con segmentadores globales y tarjetas KPI dinámicas.
*   **Fase 4 - Excel (C-Suite Ready):** Consolidación del archivo automatizado en tablas dinámicas estructuradas, manteniendo la nomenclatura técnica del pipeline de datos original como prueba de procedencia e ingeniería.
