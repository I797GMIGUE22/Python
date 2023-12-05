# DICT OR ASSOSIATIVE ARRAYS KEYS ONLY IMMUTABLE VALUES NOT LIKE DICTS OR LISTS
# DICT = AN OBJECT JAVASCRIPT
# 'key': shadhda
# NOT DUPLICATE A KEY
# Output = key value
edades1003 = {'sebastian': 30, 'daniel': 16, 'nicoll': 17, 'sarai': 16}
print(edades1003)
print(edades1003['sebastian'])
# Agregar datos
edades1003['santiago'] = 15
print(edades1003)

# Comprobar si existe una key en un dict: 'in' operator:

if 'santiao' in edades1003:
    print('encontrado')
else:
    print('no encontrado')


print('pablo' in edades1003)
