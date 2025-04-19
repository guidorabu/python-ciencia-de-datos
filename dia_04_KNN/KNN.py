def distancia(punto, nuevo_punto):
    '''Calcular la distancia entre dos puntos'''
    return sum((a - b)** 2 for a, b in zip(punto, nuevo_punto))**0.5

def knn(puntos, nuevo_punto, k= 3):
    '''Clasificar nuevo punto usando el algoritmo KNN'''
    distancias = []

    for punto, clase in puntos:
        d = distancia(punto, nuevo_punto)
        distancias.append((d, clase))

    distancias.sort(key=lambda x: x[0])

    vecinos = distancias[:k]

    clases = [clase for _, clase in vecinos]

    prediccion = max(set(clases), key=clases.count)

    return prediccion

#Prueba del algoritmo KNN

#puntos = [([1, 2], 'A'), ([2, 3], 'A'), ([3, 1], 'B'), ([6, 5], 'B')]   
#nuevo_punto = [2, 1]
#resultado = knn(puntos, nuevo_punto, k=3)
#print(f'El nuevo punto {nuevo_punto} pertenece a la clase: {resultado}')    

#personas = [([18, 1.70], 'Hombre'), ([20, 1.60], 'Mujer'), ([25, 1.80], 'Hombre'), ([30, 1.75], 'Mujer'), ([22, 1.65], 'Hombre'), ([28, 1.70], 'Mujer'), ([35, 1.80], 'Hombre')]
#nueva_persona = [29, 1.69]
#resultado = knn(personas, nueva_persona, k=3)

#print(f'La nueva persona {nueva_persona} pertenece a la clase: {resultado}')