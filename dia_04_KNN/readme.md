# Día 4: K-Nearest Neighbors (KNN)

## ¿Qué es KNN? 

Es un algoritmo de clasificación

**Idea principal:**

Un dato nuevo se clasifica segun los datos mas cercanos a él.

---

### ¿Cómo funciona?

1. Elegimos un número `k` (impar para evitar empates).
2. Medimos la **distancia** entre el dato y los datos conocidos.
3. Seleccionamos los `k` puntos más cercanos.
4. Miramos a qué clase pertenece cada uno de esos vecinos cercanos.
5. Clasificamos el nuevo dato en la **clase más común** entre los vecinos.

---

### Ejemplo 1: Clasificación de Frutas

Supongamos que tenemos frutas clasificadas por su tamaño y dulzura:

$$
\text{Frutas} = [[(\text{tamaño}_1,\text{dulzura}_1),\text{Fruta}_1],[(\text{tamaño}_2,\text{dulzura}_2),\text{Fruta}_2], ..., [(\text{tamaño}_n,\text{dulzura}_n),\text{Fruta}_n]]
$$

[2, 3] → Manzana
[7, 8] → Banana
[3, 2] → Manzana
[8, 9] → Banana

Queremos clasificar `[4, 3]` usando `k = 3`.

Buscamos las 3 frutas más cercanas y vemos qué clase es la más común.  
Si 2 son **"Manzana"** y 1 es **"Banana"**, el nuevo punto se clasifica como **"Manzana"**.


### Ejemplo 2: Clasificación por Género 

$$
\text{Personas} = [[(\text{altura}_1,\text{edad}_1),\text{genero}_1],[(\text{altura}_2,\text{edad}_2),\text{genero}_2], ..., [(\text{altura}_n,\text{edad}_n),\text{genero}_n]]
$$

Queremos clasificar a `[165, 23]` usando `k = 3`.

Calculamos las distancias, elegimos los 3 más cercanos y vemos qué género aparece más.  
Si hay 2 mujeres y 1 hombre, el resultado será: **Mujer**.