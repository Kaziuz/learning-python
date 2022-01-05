class Animal():
  def __init__(self):
    print('Animal Creado')

  def quienSoy(self):
    print('Soy un animal')
  
  def comer(self):
    print('estoy comiendo')


# clase que usa herencia
class Perro(Animal):
  def __init__(self):
    Animal.__init__(self)
    print('perro creado')
  # sobreescribimos la función en la clase Animal
  def quienSoy(self):
    print('soy un perro')

miPerro = Perro()
miPerro.quienSoy()