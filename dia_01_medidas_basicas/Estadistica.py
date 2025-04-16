#Dia 1: Mediadas estadisticas basicas

class Estadistica:

    def __init__(self, datos):
        self.datos = datos
        self.n = len(datos)

    def media(self):
        '''Calcular la media aritmética'''
        sum = 0
        for valor in self.datos:
            sum += valor
        return sum / self.n
    
    def mediana(self):
        '''Ordenar los datos y encontrar la mediana'''
        datos_ordenados = sorted(self.datos)
        mitad = self.n // 2
        if self.n % 2 == 0:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            return datos_ordenados[mitad]
        
    def moda(self):
        '''Calcular la moda'''
        '''La moda es el valor que más se repite'''
        frecuencia = {}
        for valor in self.datos:
            if valor in frecuencia:
                frecuencia[valor] += 1
            else:
                frecuencia[valor] = 1
        max_freq = max(frecuencia.values)
        modas = [x for x, v in frecuencia.items() if v == max_freq]
        return modas if len(modas) > 1 else modas[0]
    
    def varianza(self):
        '''Calcular la varianza'''
        media = self.media()
        sum_cuadrados = 0
        for valor in self.datos:
            sum_cuadrados += (valor - media) ** 2
        return sum_cuadrados / self.n
    
    def desviacion_estandar(self):
        '''Calcular la desviación estándar'''
        return self.varianza() ** 0.5
    
    def rango(self):
        '''Calcular el rango'''
        return max(self.datos) - min(self.datos)