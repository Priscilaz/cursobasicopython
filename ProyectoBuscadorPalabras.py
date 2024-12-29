
frase= input("Ingrese una frase:")
letras = []

frase = frase.lower()

letras.append(input("Ingresa la 1ra letra que quieres que cuente:").lower())
letras.append(input("Ingresa la 2da letra que quieres que cuente:").lower())
letras.append(input("Ingresa la 3ra letra que quieres que cuente:").lower())

print("\n")
print("---CANTIDAD DE LETRAS---")
c1= frase.count(letras[0])
c2= frase.count(letras[1])
c3= frase.count(letras[2])

print(f"La letra '{letras[0]}' aparece {c1} veces")
print(f"La letra '{letras[1]}' aparece {c2} veces")
print(f"La letra '{letras[2]}' aparece {c3} veces")



print("\n")
print("---CANTIDAD DE PALABRAS---")
palabras = frase.split()

print(f"La frase que ingresaste tiene {len(palabras)} palabras")

print("\n")
print("---LETRAS DE INICIO Y FIN---")
init = frase[0]
end = frase[-1]

print(f"La letra inicial es: '{init}', y la letra final es: '{end}'")

print("\n")
print("---FRASE INVERTIDA---")

palabras.reverse()
frase_invertida = ''.join(palabras)
print(f"La frase invertida es: '{frase_invertida}'")

print("\n")
print("---SE ENCUENTRA LA PALABRA PYTHON???---")
busqueda = 'python' in frase
dic = {True: 'Si', False:'No'}
print(f"La respuesta es {dic[busqueda]}")








