# map: The map function executes a specified fuction for each item in an iterable.
# The item is sent to the function as a parameter

numeros = [1, 2, 3, 4, 5]

def square(num):
  return num * 2

# for item in map(square, numeros):
#   print(item)

# si quiero la lista de vuelta
print(list(map(square, numeros)))

