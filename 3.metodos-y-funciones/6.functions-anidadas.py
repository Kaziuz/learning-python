# Una función anidada en este una function dentro de otra function
# variable global
name = 'alexander'

def saludo():
  # hacemos referencia a la variable global
  global name
  print(f'name es {name}')
  def hola():
    global name
    name = 50
    print(f'hola {name}')
  hola()

saludo()