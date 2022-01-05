# Listas
mi_lista = ['hola', 2, 3]
otra_lista = ['cuatro', 'cinco']

print(mi_lista)      # output: ['hola, 2, 3]
print(len(mi_lista)) # output: 3
print(mi_lista[0])   # output: 'hola'
print(mi_lista[1:])  # output: [2, 3]
print(mi_lista + otra_lista) # output: ['hola', 2, 3, 'cuatro', 'cinco']

nuevo_lista = mi_lista + otra_lista
nuevo_lista[0] = 'alex' # reemplazo lo que hay en el indice 0
print('nueva lista: {}'.format(nuevo_lista))

# Para concatenar, agregar nuevos items a la lista
nuevo_lista.append('seis')
print(nuevo_lista)

# Para quitar elementos de una vista, si queremos un item especifico añadimos el index
# nuevo_lista.pop(1)
# tambien podemos añadir indices negativos
item_cortado = nuevo_lista.pop(-2)
print(item_cortado)
print(nuevo_lista)

print('------------------------')

# Para ordenar items de una lista usamos .sort()
letras = ['a','z','w','c','b','o','t']
numeros = [90, 5, 1, 78, 3, 6, 4, 8]

# si hacemos letras_ordenadas = letras.sort() nos va a salir un NONE
letras.sort()
numeros.sort()
print(letras)
print(numeros)

# Para retornar el reverso de la matrix usamos .reverse()
letras.reverse()
numeros.reverse()
print('reversados')
print(letras)
print(numeros)
