# Día 1: Medidas estadísticas básicas

## Algortimos implementados

### Medidas de tendencia central
- Media
- Mediana
- Moda
### Medidas de dispersión
- Varianza
- Desviación estándar
- Rango

## Fórmulas
### Medidas de Tendencia Central

--- 

- **Media**

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

- **Mediana**
Si *n* es impar: 

$$
\text{Mediana} = x_{\left(\frac{n+1}{2}\right)}
$$

Si *n* es par:  

$$
\text{Mediana} = \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)}}{2}
$$

- **Moda**

$$
Moda = \text{valor más frecuente del conjunto de datos}
$$

---

### Medidas de Disperción

--- 

- **Varianza**

Poblacional:

$$
\sigma^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$  

Muestral:  

$$
s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

- **Desvio estandar**

Poblacional:  

$$
\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}
$$  
Muestral: 

$$
s = \sqrt{\frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

- **Rango**

$$
\text{Rango} = x_{\text{máx}} - x_{\text{mín}}
$$

---

## Descripción
En el Día 01 trabaje con medidas estadísticas basicas. Implemente los algoritmos sin utilizar librerías externas para entender la logica de cada cálculo y practicas de programación en Python.

### Fichero Dia 01
`Estadistica.py`: contiene una clase `Estadistica` que permite calcular las medidas de tendencia central y medidas de disperción sobre una lista de datos.