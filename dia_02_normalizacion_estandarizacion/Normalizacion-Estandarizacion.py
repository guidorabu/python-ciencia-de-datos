def normalizar(datos):
    '''Normaliza los datos a un rango entre 0 y 1. '''
    dato_min = min(datos)
    dato_max = max(datos)
    return [(dato - dato_min) / (dato_max - dato_min) for dato in datos]

def estandarizar(datos):
    '''Estandariza los datos a una media de 0 y desviación estándar de 1. '''
    media = sum(datos) / len(datos)
    varianza = sum((dato - media) ** 2 for dato in datos) / len(datos)
    desviacion = varianza ** 0.5
    return [(dato - media) / desviacion for dato in datos]

#prueba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print("Datos originales: ", prueba)
#print("Datos normalizados: ", normalizar(prueba))
#print("Datos estandarizados: ", estandarizar(prueba))
