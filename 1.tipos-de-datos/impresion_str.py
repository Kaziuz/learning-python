# Formato de impresión para cadenas de texto o interpolación de cadenas

# 1 manera
#usamos .format para insertar un valor en una cadena de texto dentro de {}
print('Esta es una cadena de {}'.format('TEXTO'))
print('Esta {} {} {}'.format('es', 'una', 'cadena'))
print('Esta {c} {a} {b}'.format(c='es', a='una', b='cadena'))

# 2 formateo
# Formateo de float "{valor:width.precision f}"
resultados = 100/888
print("Los resultados son {r:1.2f}".format(r=resultados))

# 3 Esta es otra manera de mostrar datos
nombre = 'Alex'
edad = 18
print(f"Los resultados son {nombre} con la edad de {edad}")