def media(datos);
    '''Calcular la media'''
    return sum(datos) / len(datos)

def calcular_pendiente(x, y):
    '''Calcular la pendiente de la recta de regresion'''
    x_media = media(x)
    y_media = media(y)

    numerador = sum((xi - x_media) * (yi - y_media) for xi, yi in zip(x, y))
    denominador = sum((xi - x_media) ** 2 for xi in x)

    return numerador / denominador

def calcular_ordenada(x, y, m):
    '''Calcular la ordenada al origen de la recta de regresion'''
    x_media = media(x)
    y_media = media(y)

    return y_media - m * x_media

def predecir(x, m, b):
    '''Predecir el valor de y dado x, la pendiente y la ordenada al origen'''
    return m * x + b

