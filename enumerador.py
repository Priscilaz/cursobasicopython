#SIN uso de ENUMERATOR
lista = ['a','b','c']
indice =0

for item in lista:
    print(indice, item)
    indice +=1


#Uso de ENUMERATOR
lista1 = ['a','b','c']
for indice, item in enumerate(lista1):
    print(indice, item)
#Lista de tuples
mis_tuples= list(enumerate(lista1))
print(mis_tuples)


"""Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombre in enumerate(lista_nombres):
    if nombre[1].startswith('M'):
        print(nombre[0])