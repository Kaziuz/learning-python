# Diccionarios: es como un objeto json en javascript
mi_diccionario = {'manzana': 2.90, 'agua': 5.40, 'lote': { 'nombre': 'exito'}, 'carnes': ['hamburguesa', 'res', 'cerdo'] }
print(mi_diccionario)

# Para acceder a una llave especifica del objeto
print(mi_diccionario['carnes'])

# Para agregar nuevas keys
mi_diccionario['nueva_key'] = 400
print(mi_diccionario)

# Para ver todas las llaves de un diccionario .keys()
print('llaves del diccionario: {}'.format(mi_diccionario.keys()))

# Para ver todos los valores de las llaves del dictionario .values()
print('values: {}'.format(mi_diccionario.values()))

# para ver los pares de un diccionario .items()
print('items: {}'.format(mi_diccionario.items()))
