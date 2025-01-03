#-- *args
#Funciones genericas con argumentos variables
#def suma(a,b):
#   return a+b
#esto generaria el error:
#print(suma(2,5,8))
#TypeError: suma() takes 2 positional arguments but 3 were given

#Aplicacion de *args
"""def suma(*args):
    total =0
    for arg in args:
        total += arg
    return total
    #Tambien puedo reemplazar todo por
    #return sum(args)
print(suma(2,10,8))"""
from itertools import count

"""def suma_cuadrados(*args):
    suma =0
    for arg in args:
        suma += arg ** 2
    return suma


print(suma_cuadrados(1, 2, 3))"""


"""def suma_absolutos(*args):
    sum =0
    for arg in args:
        sum += abs(arg)
    return sum

print(suma_absolutos(1, -8, 2))"""


#--------/// **kwargs
"""def suma(**kwargs):
    total =0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3, y=5, z=2))"""


#Mezclando todos los tipos de argumentos
"""def prueba(n1, n2, *args, **kwargs):
    print(f"El primer valor es {n1}")
    print(f"El segundo valor es {n2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")



prueba(15,50,1,2,3,4, x=3, y=5, z=2)"""


"""def cantidad_atributos(**kwargs):

    for arg in kwargs.items():
        r=0
        r=len(kwargs)
    return r


print(cantidad_atributos(x=2,a=5,b=6,c=0))"""


"""def lista_atributos(**kwargs):
    valores = []
    for clave, valor in kwargs.items():
        valores.append(valor)
    return valores


print(lista_atributos(v1='Ana', v2='Paola', v3='Juanito'))"""

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

describir_persona("María", color_ojos="azules", color_pelo="rubio")








