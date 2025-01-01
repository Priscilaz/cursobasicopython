from random import *
n=0
elegido = randint(1,101)

print('Hola, Bienvenido al juego!\n'
      'tendras que adivinar el numero que estoy pensando en 8 intentos!')

for i in range(1,9):

    n=int(input("Ingresa un numero: "))
    match n:
        case _ if n not in range(1,101):
            print("El numero se sale del rango permitido.....")
        case _ if n > elegido:
            print("Has elegido un numero mayor al que estoy pensando....")
        case _ if n < elegido:

            print("Has elegido un numero menor al que estoy pensando....")
            if i ==8:
                print(f"Y te quedaste sin intentos,oh no adivinaste.......\n"
                      f"el numero era: {elegido}")

        case _ if n == elegido:
            print(f"Felicidades, ese era el numero que pense, \n lo lograste en {i} intentos")
            break

        case _ :
            print(f"Y te quedaste sin intentos,\n"
                      f"el numero era: {elegido}")
