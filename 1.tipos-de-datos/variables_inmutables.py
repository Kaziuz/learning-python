#variables Inmutables
# En python las cadenas no se pueden editar 
name = 'Pam'
# name[0] = 'S'

primera_letra = name[:1]
ultimas_letras = name[1:]

print('P' + ultimas_letras)

letra = 'Z'
letra = letra * 10

print(letra)

# python es flexible pero eso es bueno y malo
# malo porque aqui no suma pero nos da un resultado
suma = '1' + '2'
print('suma:' + suma)

x = 'hola mundo'
x = x.upper()
print(x) # output = HOLA MUNDO

x = x.lower()
print(x) # output = hola mundo

x = x.split()
print(x) # output: ['hola', 'mundo']

x = 'hola mundo'
x = x.split('o') # en este caso decimos partir por la letra o y ademas python la elimina
print(x) # ['h', 'la mund', '']

x = 'hola|mundo'
x = x.split('|')
print(x) # ['hola', 'mundo']
