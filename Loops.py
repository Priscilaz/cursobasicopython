"""lista = ['a','b','c']

for letra in lista:
    numero_letra = lista.index(letra) +1
    print(f"Letra {numero_letra}:  {letra}" )

lista = ['pablo','laura','fede','luis','julia']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("Nombre que no empieza con 'L'")"""

"""numeros = [1,2,3,4,5]
mi_valor =0

for numero in numeros:
    mi_valor= mi_valor+numero
    print(mi_valor)"""

palabra = 'python'
#for letra in palabra:
    #print(letra)
#for objeto in [(1,2),3,4,5]:
    #print(objeto)

for a,b in [(1,2),(3,4),(5,6)]:
    print(a)
    print(b)
    #Si quiero solo el 1er elemento ce cada sub lista
    #solo debo poner print(a)

dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}

for item in dic.items(): #o.values()
    print(item)