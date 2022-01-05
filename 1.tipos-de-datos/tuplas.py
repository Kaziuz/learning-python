# Tuplas
# Son similares a las listas. Se diferencian porque son inmutables
# Una vez que un element se encuentra en la tupla no puede ser reasignado
# Las tuplas usan parentesis (1,2,3)
# Las listas usan corchetes [1,2,3]

tupla = ('a','b','c','a')
lista = [1,2,3]
print(type(tupla))

# Podemos procesar una tupla como procesamos una lista
print(tupla[0:2])

# Con las tupla podemos hacer conteos
print(tupla.count('a'))

# Nos retorna el primer indice que encuentra de una busqueda
print(tupla.index('a'))

# una tupla no se puede reasignar, es inmutable
# esta linea de código causara un error
# tupla[0] = 'ale'
print(tupla)
