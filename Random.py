from random import *

#aleatorio = randint(1,50)
#print(aleatorio)

aleatorio1 = round(uniform(1,5),2)
print(aleatorio1)

#---Valores entre 0 y 1
al = random()
print(al)

#---choice
colores = ['azul','verde','rojo','lila']
aleatorio = choice(colores)
print(aleatorio)

#--Shuffle no para strings
numeros = list(range(5,50,5))
shuffle(numeros) #genera una mezcla aleatoria
print(numeros)