# TODO DATO ES UN OBJETO
b = 2
d = '6'
# LIST = ARRAY
conjunto = ['0', 1, b, 3, int("5")]
print(conjunto)

print()
# Se inserta en la posicion 4 un 4
conjunto.insert(4, 4)
print(conjunto)

print()
# Se agrega al final de la lista el string 6
conjunto.append(d)
print(conjunto)

print()
# Se extrae el ultimo dato de la lista
numero6 = conjunto.pop()
print(numero6)
print(type(numero6))
conjunto.pop() # y ota vez
print(conjunto)

print()
# inicio:fin:salto
print(conjunto[1:5:2])

print()
# LIST.REMOVE()
print('Se elimina el 0 del array')
conjunto.remove("0")
print(conjunto)

print()
# TUPLE is a list but it is NOT MODIFICABLE
print('Comparacion entre a list and a tuple')
print()
conjTuple = (1,2,3,4,5,6)
print(conjTuple)
print(type(conjTuple))
print()
print(conjunto)
print(type(conjunto))

# Tuple = (not modificable) != list = [modificable]
