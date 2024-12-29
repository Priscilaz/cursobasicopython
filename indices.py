#mi_texto = "Esta es una prueba"
#resultado = mi_texto[0]
#print(resultado)
#resultado = mi_texto[-4]
#print(resultado)
#resultado = mi_texto.index("prueba")
#print(resultado)
##Decirle desde donde empiece a buscar
#resultado = mi_texto.index("a",5)
#print(resultado)
#Cuenta desde el final
#resultado = mi_texto.rindex("a")
#print(resultado)

##Slicing
texto = "ABCDEFGHIJKLM"
fragmento = texto[2]

texto = "ABCDEFGHIJKLM"
#Desde el indice 2 hasta el 5 pero no incluyendo al 5
"""fragmento = texto[2:5]
print(fragmento)

#Desde el indice 2 hasta el final
fragmento = texto[2:]
print(fragmento)

#Desde el comienzo hasta el indice 5 pero no incluyendolo
fragmento = texto[:5]
print(fragmento)

#3ER parametro indica cada cuantos caracteres voy a ir extrayendo
fragmento = texto[2:12:2]
print(fragmento)
#Toda la cadena pero al reves
fragmento = texto[::-1]
print(fragmento)"""



###Metodos String
texto = "Este es el texto de ejemplo"
"""resultado = texto
print(resultado)

#Upper lo mismo con lower
resultado = texto[1].upper()
print(resultado)

#Split
resultado = texto.split("o")
print(resultado)

#Join
a = "Aprender"
b = "Python"
c = "es"
d= "cool"
e = " ** ".join([a, b, c, d])
print(e)

#Find retorna posicion si lo encuentra, -1 si no 
resultado = texto.find("texto")
print(resultado)"""

#Replace
#resultado = texto.replace("texto", "libro")
#print(resultado)


##Propiedades de los Strings
nombre = "Carina"

#print(nombre * 3)
poema = """Mil pequeños peces blancos 
como si hirviera
el color del agua"""
print(poema)
#Retorna boolean
print("agua" in poema)
print("agua" not in poema)

#Length
var = "gato loco"
print(len(var))