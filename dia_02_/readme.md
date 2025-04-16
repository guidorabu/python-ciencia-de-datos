# Día 2: Normalización y Estandarización de Datos

Este día codifique dos técnicas fundamentales de la estadística, muy utilizadas para el prerpocesamiento y procesamiento de datos: **normalización** y **estandarización**. Ambas permiten **escalar** los datos para que puedan ser utilizados de manera más efectiva por algortimos de **machine learning** y de **análisis estadístico**

--- 

## Objetivos

- Implementar desde cero las funciones para normalizar y estandarizar una lista de datos cuantitativos.
- Entender las diferencias conceptuales y matemáticas entre normalización y estandarización.

---

## Definiciones

- **Normalización (Min-Max Scaling):** escala los datos para que estén en un rango entre 0 y 1.

Fórmula:

\[
x_{norm} = \frac{x - x_{min}}{x_{max}- x_{min}}
\]

--**Estandarización (Z-Score Scaling):** transforma los datos para que tengan una media 0 y una desviación estándar 1.

Fórmula:

\[
x_{est} = \frac{x - \mu}{\sigma}
\]

---

Archivo: `Normalizacion-Estandarizacion.py`