class Animal():
  def __init__(self):
    print('Animal Creado')
  def quienSoy(self):
    print('Soy un animal')
  def comer(self):
    print('estoy comiendo')


class Perro(Animal):
  def __init__(self):
    Animal.__init__(self)
    print('perro creado')
  def quienSoy(self):
    print('soy un perro')