"""def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range (100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras


resultado = chequear_3_cifras([555,99,600])
print(resultado)"""

"""lista_numeros = [5,52,-54,100,8,99]
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False

    return True

resultado = todos_positivos(lista_numeros)
print(resultado)"""

#--Ejercicio desempacar tuples
#- Sin FUnciones
precios_cafe = [('capuccino',1.5),('expresso',2.2),('mocca',1.9)]

"""for cafe, precios in precios_cafe:
    print(precios*0.45)"""

#Ahora quiero una funcion que vaya
#almacenando el precio mayor

"""def cafe_mas_caro(lista_precios):
    precio_mayor =0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)

print(cafe_mas_caro(precios_cafe))"""



#######################################################
######################################################
####//**--------INTERACCION ENTRE FUNCIONES---------**\\

"""from random import shuffle
#lista inicial
palitos = ['-','--','---','----']

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return  lista

#pedir al usuario el intento
def probar_suerte():
    intento = ' '
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)




#comprobar el intento

def chequear_intento(lista, intento):
    if lista[intento-1] == '-':
        print("Perdiste")
    else:
        print("Te salvaste")

    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)

seleccion = probar_suerte()

chequear_intento(palitos_mezclados, seleccion)"""


"""Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función 
debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
"""

"""from random import *
def lanzar_dados():
    n1 = randint(1,6)
    n2 = randint(1,6)
    return n1,n2

#suma_dados=0

def evaluar_jugada(v1, v2):
    suma_dados = v1 + v2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    else:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"

n1, n2 = lanzar_dados()
juego = (evaluar_jugada(n1, n2))
print(juego)"""


"""Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda 
al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
"""
from random import *


def lanzar_moneda():
    opc = ['Cara', 'Cruz']
    rpta = choice(opc)
    return rpta


lista_numeros = [1, 4, 6, 7, 8, 9, 33, 10]


def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        lista = lista_numeros.clear()
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista
















