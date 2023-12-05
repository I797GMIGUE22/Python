print("hola mundo ñ")
a = "3"
b = 4
c = [a, b, "akka"]
d = 1.0
clave = 'secreto'

#Declaracion e inicializacion de varias variables a la vez

e, f, g, h = "la vaca Lola", 3, 4, 4.4
edad = input('Edad: ')

print(type(a))
print(edad)
print(int(edad)* 4 * int(a))

entrada = input('Ingresa la clave: ')

if (entrada == clave):
    print('Hurra')
else:
    print(type(entrada))
    print('ERROR')
    

print()
#Signo de potenciacion
potencia = 3**2

print(potencia)

print()
#Signo de division entera: Sin decimales

sinDecimales = 3//4

print('Division entera: Sin decimales: ')

print(sinDecimales)
print(type(sinDecimales))

print()
conDecimales = 3/4

print('Division normal: Con decimales: ')

print(conDecimales)
print(type(conDecimales))

#Signo de modulo: Residuo

w = 3%2

print(w)
