# While
# El else significa que el ciclo ha terminado

# x = 0
# while x < 6:
#   print(f'El valor actual de x es: {x}')
#   x += 1
# else: # Nos indica que el ciclo for a terminado
#   print('X no es mayor a 6')

# Tenemos tres palabras reservadas para los ciclos for: break, continue, pass
# PASS:La declaración pass se utiliza como marcador de posición para el código futuro.
# Cuando se ejecuta la instrucción pass, no sucede nada,
# pero evita obtener un error cuando no se permite el código vacío.
x = [1, 2, 3]
for item in x:
  pass
print('Fin del libreto')

# CONTINUE: La palabra clave continue se usa para finalizar
# la iteración actual en un ciclo for (o un ciclo while) y continúa con la siguiente
# iteración. Para este ejemplo no contamos la letra y
n = 'johnny'
for letter in n:
  if letter == 'y':
    continue
  print(letter)

# BREAK: la palabra clave break se usa para romper un ciclo for o un ciclo while
# En el ejemplo, entramos si llegamos a i, salimos del ciclo
k = 'toñis'
for letter in k:
  if letter == 'i':
    break
  print(f'\n{letter}')