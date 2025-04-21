import sys
sys.path.append('./dia_01_medidas_basicas')

from Estadistica import Estadistica


mis_datos = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]

mis_datos = Estadistica(mis_datos)


# Imprimir los resultados de las medidas estadísticas
print("Datos:", mis_datos.datos)
print("Media:", mis_datos.media())
print("Mediana:", mis_datos.mediana())
print("Moda:", mis_datos.moda())
print("Varianza:", mis_datos.varianza())
print("Desviación estándar:", mis_datos.desviacion_estandar())
print("Rango:", mis_datos.rango())
