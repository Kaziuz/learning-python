# Cadenas de texto
print('cadena de texto simple')
print("cadena de texto simple 'compleja'")
print('hola \nmundo') # asi se hace para generar un enter en consola
print(len('hola')) # el len es como el length en javascript, nos da la longitud

# Indexado de cadenas
print('------------------------\n')
string_ind = 'hola mundo'
print(string_ind[3])  # de esta manera accedo a cada letra de la cadena
print(string_ind[-1]) # con el indexado inverso, de esta forma acceso al último caracter

# Slicing de cadenas
print('------------------------\n')
mi_string1 = 'Este es un texto largo'
# micadena[start:stop:step]
print(mi_string1[0:3]) # output -> Est
print(mi_string1[0:4])
print(mi_string1[0:4:2])
print(mi_string1[11:22])
