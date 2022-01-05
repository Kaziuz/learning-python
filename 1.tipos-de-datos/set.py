# Sets
# Es muy importante recalcal que solo guarda valores unicos
mi_set = set()

# para añadir un elemento
#mi_set.add(1)
#print(mi_set)

# Para añadir varios elementos
# se hace de la forma de abajo, porque asi mi_set.add(1, 2) no se puede
mi_set.add(1)
mi_set.add(2)
print(mi_set)

# Podriamos usar un set para ver los valores unicos de una lista
mi_lista = [1,1,1,1,3,3,3,3,6,6,6,6,8,8,8,2,2,2,2,9,9,9,9,10]
print(set(mi_lista))
