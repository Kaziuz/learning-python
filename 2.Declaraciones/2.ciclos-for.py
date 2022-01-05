# Ciclos for
numeros = [1,2,3,4,5,6,7,8,9,10]
suma = 0

# for numero in numeros:
#   suma = suma + numero
#   if numero % 2 == 0: # chequiamos si el numero es par
#     print(f'número par: {numero}')
#   else:
#     print(f'número inpar: {numero}')
#   print(f'suma: {suma}')

# for letter in 'Hola Mundo':
#   print(letter)

tuplas = [(1,2),(3,4),(5,6),(7,8)]

# for tupla in tuplas:
#   print(tupla) # me salen los pares

# for (a, b) in tuplas:
#   print(a)
#   print(b)

# ciclos for a diccionarios
diccionario = {'uno':1, 'dos':2, 'tres':3}
for (key,value) in diccionario.items():
  print(key)
  print(value)
for item in diccionario.items():
  print(item)