# Día 5: Regresión Lineal simple

## ¿Qué es la REgresión Lineal Simple?

Es una técnica estadística que permite **predecir un valor (y)** a partirde **otros valor (x)**, asumiendo que existe una **relacion lineal** entre ellos.

La fórmula general es: 

$$
y = m \cdot x + b
$$

Donde: 

- `m` es la **pendiente* (indica cuánto varía `y` cuando cambia `x`).
- `b` es la **ordenada al origen** (el valor `y` cuando `x = 0`).

---

### ¿Cómo se calcula?

1. Se calcula la **media de `x` y de `y`.
2. Se halla la **pendiente (m)** con la fórmula:

$$
m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
$$

3. Luego se calcula la **ordenada al origen**:

$$
b = \bar{y} - m \cdot \bar{x}
$$

4. Finalmente, se puede **predecir un nuevo valor `y` dado un valor de `x`:

$$
y = m \cdot x + b
$$

---

## Ejemplo práctico

Supongamos que tenemos los siguientes datos:

- **x** = [1, 2, 3, 4, 5]  (horas de estudio)  
- **y** = [2, 4, 5, 4, 5]  (nota del examen)

Podemos calcular la recta de regresión y luego predecir la nota esperada si alguien estudia 6 horas.
