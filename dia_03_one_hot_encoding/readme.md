# Día 3: One-Hot Encoding

## ¿Qué es el One-Hot Enconding?

El One-Hot Encoding es una técnica de preprocesamiento que transforma variables categóricas en vectores vinarios. Cada categoría única se representa como una nueva columna, con valores:

* `1` si la categoría está presente en ese registro.
* `0` en caso contrario.

### Ejemplo básico

['Rojo', 'Verde', 'Azul']

El One-Hot Encoding generaría una matriz:

Rojo        Verde       Azul
---
 [1, 0, 0] 
 [0, 1, 0]
 [0, 0, 1] 
 ## ¿Tiene límites el One-Hot Encoding?

 En teoría:
 No, se podría aplicar One-Hot a tantas categorías como quieras.

 Pero en la práctica:
 Sí, hay limitaciones prácticas:

Muchas categorías únicas ---> Generarian muchas columnas

Esto haría muy costosa la implementacion debido al uso de memoria. 