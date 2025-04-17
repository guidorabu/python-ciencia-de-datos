def one_hot_enconde(lista):
    categorias = list(dict.fromkeys(lista))
    codigos = []
    for item in lista:
        vector = [1 if item == categoria else 0 for categoria in categorias]
        codigos.append(vector)
    return categorias, codigos

#Pruebas

#colores = ['rojo', 'verde', 'azul', 'verde', 'rojo'] 

#categorias, codificado = one_hot_enconde(colores)
#print(categorias) 
#print('codificacion one-hot:')
#for i in codificado:
#    print(i)

#autos = [ 'mercedes', 'audi', 'bmw', 'mercedes', 'audi', 'ford', 'ford', 'ford', 'fiat', 'renault', 'renault', 'ford', 'mercedes', 'audi', 'bmw', 'mercedes', 'audi', 'ford', 'ford', 'ford', 'fiat', 'renault', 'renault']

#categorias, codificado = one_hot_enconde(autos)
#print(categorias)
#print('codificacion one-hot:')
#for i in codificado:
#    print(i)