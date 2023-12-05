c = {'perro': 3, 'gato': 6, 'mono': 8, 'gorilla': 12}

print(c)

c['jirafa'] = 2

print(c)

busqueda = input('Ingresa la clave a buscar: ')

if(busqueda in c):
    print('Encontrado')
else:
    print('No fue encontrado')
