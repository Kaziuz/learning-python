# Operadores utiles

# for num in range(10): # Es una forma rapida de imprimir los numeros del cero al 10
#   print(num)

# for num in range(0,11,2): # Decimos que cuente de cero hasta 11 de a dos
#   print(num)

# print(list(range(0,11,2))) # construimos una lista de esta forma [0,2,4,6,8,10]

# Cuando trabajmos en python es bueno iterar de esta manera: usando enumerate
# La función enumerate() toma una colección y la devuelve como un objeto enumerado
# La función enumerate() agrega un contador como clave del objeto enumerado
# palabra = 'hola'
# for item in enumerate(palabra):
#   print(item)

# Para emparejar dos tuplas o dos listas usamos zip()
# si hay una tupla o una lista mas larga que otra, la de menor elementos decidira la nueva longitud del zip iterado
# lista1 = [1,2,3]
# lista2 = ['a','b','c']

# for item in zip(lista1, lista2):
#   print(item)

# # para generar una lista con tupas de lista1 y lista2
# print(list(zip(lista1, lista2)))

# Podemos preguntar si existe una letra en un array o en un diccionario
lista2 = ['a','b','c']
dic = { 'k1': 1 }

if 'a' in lista2:
  print('verdadero')
if 'k1' in dic:
  print('verdadero')
if 'k1' in dic.keys():
  print('veradero')




