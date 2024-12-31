nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'Madrid', 'Quito']
combinados = list(zip(nombres,edades,ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre}, tiene {edad} anios y vive en {ciudad}")


"""Crea el zip con las traducciones los números del 1 al 5 en español,
 portugués e inglés (en el mismo orden), y convierte el objeto generado 
 en una lista almacenada en la variable numeros:
1: uno / um / one
2: dos / dois / two
3: tres / três / three
4: cuatro / quatro / four
5: cinco / cinco / five"""

espanol= ['uno', 'dos', 'tres', 'cuatro','cinco']
portugues= ['um', 'dois', 'três', 'quatro','cinco']
ingles =['one','two','three','four','five']

numeros = list(zip(espanol, portugues, ingles))
print(numeros)