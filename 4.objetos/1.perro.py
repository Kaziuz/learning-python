class Perro():
  # este metodo es requerido porque aqui definimos los atributos a usar
  # el parametro self es una referencia a las instancia de la clase
  def __init__(self, raza, nombre, puntos):
    # atributos
    self.raza = raza
    self.nombre = nombre

    # valor booleano
    self.puntos = puntos
  
  # Cuando se crea una function de un objeto
  # es necesario agregar la palabra self en los parametros
  def ladrar(self):
    print(f'{self.nombre} ladrando')

doberman = Perro(raza='doberman',nombre='Sam',puntos=False)
print(f'el perro se llama {doberman.nombre} de raza {doberman.raza} y {doberman.puntos} en puntos')
doberman.ladrar()