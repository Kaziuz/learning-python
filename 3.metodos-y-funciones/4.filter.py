# filter: La function filter devuelve un iterador donde los elementos
# se filtran a través de una función para probar si el elemento
# e aceptado o no

numeros = [1,4,3,7,10,12, 23]

def myFunc(num):
  # check number is par
  return num%2 == 0

# for n in filter(myFunc, numeros):
#   print(n)

print(list(filter(lambda num: num%2 == 0, numeros)))

