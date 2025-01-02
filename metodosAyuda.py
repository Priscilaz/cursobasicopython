#-- La funcion lstrip elimina por izq los caracteres
# que yo le especifique

frase = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
frase_nueva = frase.lstrip(",:_#%")
print(frase_nueva)

#--Añade el elemento "naranja" como el cuarto
# elemento de la siguiente lista "frutas", utilizando
# el metodo insert

frutas = ["mango", "banana", "cereza",
          "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)

#"""Verifica si los sets a continuación forman
# conjuntos aislados (es decir, que no tienen
# elementos en común), utilizando el metodo
# isdisjoint(). Almacena dicho resultado en la
# variable conjuntos_aislados:"""

##-- Este metodo retorna True si es que no hay elementos en comun
# y retorna false si es que si los hay
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
respuesta = {True: 'No hay elementos en comun', False: 'Hay elementos en comun'}
print(conjuntos_aislados)
print(f"El resultado es:  {respuesta[conjuntos_aislados]}")