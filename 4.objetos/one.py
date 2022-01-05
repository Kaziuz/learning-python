# Para entender el funcionamiento de __name__ y __main__

def func():
  print('func() en uno.py')

print('nivel top en uno.py')

if __name__ == '__main__':
  print('uno.py esta siendo corrido directamente')
else:
  print('uno.py esta siendo importado')