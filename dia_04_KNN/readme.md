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