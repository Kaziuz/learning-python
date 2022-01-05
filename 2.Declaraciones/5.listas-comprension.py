# Listas de comprensión
# La comprensión de listas ofrece una sintaxis más corta
# cuando desea crear una nueva lista basada en los valores de una lista existente.
# -----------------------------------------------------------
# Si nos encontramos usando un ciclo for con .append()
# podemos usar una comprensión en su lugar para hacerlo mas eficiente

# Normalmente para llenar un array con algo se haria de esta forma
# mi_cadena = 'hola'
# mi_lista = []
# for letter in mi_cadena:
#   mi_lista.append(letter)

# print(mi_lista)

# De esta manera hacemos lo mismo que lo anterior, esta sintaxis es unica de python
mi_lista = [letter for letter in 'hola']
print(mi_lista)

# numeros = [x+x for x in range(0, 11)]
# print(numeros)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]

# print(newlist)