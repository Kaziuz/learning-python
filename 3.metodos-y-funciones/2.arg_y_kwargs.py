# Los *args son para pasarle lo que sea a una function como parametros, trabajan en forma de tuplas
def sumar(*args):
  # retornamos el 5% de una suma
  return print (sum(args) * 0.05)

#sumar(40, 50, 12, 78, 100)

# Los **kwargs trabajan en forma de diccionario
def fruta(**kwargs):
  if 'fruit' in kwargs:
    print('Mi fruta escogida es {}'.format(kwargs['fruit']))
  else:
    print('No hay fruta')

#fruta(fruit='kiwi', veggie='lechuga')

# Usamos ambas juntas
def func(*args, **kwargs):
  print(args)
  print(kwargs)
  print('Me gustaria {} {}'.format(args[0], kwargs['comida']))

func(10, 30, 50, comida='leche', animal='perro')

