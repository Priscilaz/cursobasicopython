#Antes de aplicar
palabras = 'python'
lista = []
for letra in palabras:
    lista.append(letra)
print(lista)

#Despues de aplicar
#letra es una variable temporal, debe ser igual
# las dos veces que se escribe
palabra = 'python'
lista = [letra for letra in palabra]
print(lista)
# o tambien
lista = [letra for letra in 'python']

#-Con enteros
lista = [n*2 for n in range(0,21,2) if n*2>10]
print(lista)

#Si quiero con if y else
lista2 = [n if n*2>10 else 'NO' for n in range(0,21,2) ]
print(lista2)

pies = [10,20,30,40,50]
metros = [p *3.281 for p in pies]
print(metros)

"""Crea una lista valores_pares formada 
por los números de la lista valores que 
(¡adivinaste!) sean pares.
"""
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [v for v in valores if v %2 ==0]
print(valores_pares)