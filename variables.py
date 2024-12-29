#Seccion 2
#nombre = "Juan"
#print(nombre)
#nombre = "Laura"
#print(nombre)
from traceback import print_tb

#edad= 30
#edad1= 12
#print (edad + edad1)

#nombre=input("Dime tu nombre: ")
#print("Tu nombre es: " + nombre)

#mi_numero = 1
#print(mi_numero)

#print(type(mi_numero))

#nombre= "Teresa"
#print(nombre + nombre)
#print(type(nombre))

#edad = input("Ingresa tu edad: ")
#print(edad + edad)
#num1 =7.5
#num2 =2.5
#print(type(num1 + num2))

#Conversiones
##Implicitas
#num1 = 20
#num2 = 30.5

#num1 = num1 + num2
#print(type(num1))
#print(type(num2))
#print(type(num1 + num2))

#num1 = 5.8
#print(num1)
#print(type(num1))

#num2 = int(num1)
#print(num2)
#print(type(num2))

#edad = input("DIme tu edad: ")
#print(type(edad))
#edad = int(edad)
#print(type(edad))
#nueva_edad = 1 + edad
#print(nueva_edad)
#print(type(nueva_edad))

##Formatear cadenas
#x = 10
#y = 5
#concatenando
#print("Mis numeros son " + str(x) + " y " + str(y))
#formateando
#print("Mis numeros son {} y {}".format(x,y))

#print("La suma de {} y {} es {}".format(x,y, x+y))


#color = "rojo"
#matricula = 541923
#print(f"El auto es {color} y su matricula es {matricula}")


##Operadores
x = 6
y = 2
z = 7

#print(f"{x} mas {y} es igual a {x+y}")
#print(f"{x} menos {y} es igual a {x-y}")
#print(f"{x} por {y} es igual a {x*y}")
#print(f"{x} entre {y} es igual a {x/y}")
#print(f"{x} elevado a {y} es igual a {x**y}")

##De una division truncar a entero
#print(f"{z} dividido entre {y} es igual a {z//y}")

##Modulo
#print(f"{z} modulo de {y} es igual a {z%y}")

#Potencia cubica
#print(f"{x} elevado a la {3} es igual a {x**3}")

#Raiz cuadrada
#print(f"La raiz cuadrada de {6} es {x**0.5}")

#Redondeo
#resultado = round(90/7)
#print(resultado)

#valor = 95.666666666
#print(valor)
#print(type(valor))

#print(round(valor))

##Proyecto Seccion 2
nombre = input("Ingresa tu nombre:")
ventas = float(input("Ingresa tus ventas totales del mes: "))
comision = round(ventas * 13 / 100,2)

print(f"Estimado/a {nombre}, las comisiones que"
      f" recibiras este mes \nes de: $ {comision}")

