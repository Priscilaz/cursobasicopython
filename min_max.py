menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
#print(menor)
#print(mayor)

lista = [58,96,72,64,35,100]
#print(f"El menor es: {min(lista)}, y el mayor es: {max(lista)}")

nombres = ['juan','pablo','alicia','carlos']
print(min(nombres))

#El primer caracter, primero busca las MAYUSC
nombre = "Priscila"
print(min(nombre.lower()))

dic = {'c1':45, 'c2':11}
print(min(dic.values()))


diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}


"""Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

Almacena dicho valor en una variable llamada edad_minima.

También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre."""
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())

print(edad_minima, ultimo_nombre)