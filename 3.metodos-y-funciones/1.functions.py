# funciones

# def decirHola():
#   print('hola')
#   print('como')
#   print('estas')

# decirHola()

# def suma(num1, num2):
#   total = num1 + num2
#   print(total)

# suma(4, 5)

# buscamos numeros pares en lista
def numeroPar(numList):
  for number in numList:
    if number % 2 == 0:
      print('True')
      return True
    else:
      pass
  print('False')
  return False

numeroPar([1, 2, 6])