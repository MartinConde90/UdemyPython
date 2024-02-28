from random import *

num_aleatorio = randint(1,101)
#print(num_aleatorio)
intentos = 0
numero_usuario = 0
nombre_jugador = input("Introduce tu nombre: ")

print(f"Hola {nombre_jugador}, he pensado un número entre 1-100. \nTienes 8 intentos para adivinarlo.")

while intentos < 8:
    intentos += 1
    print(f"Intento->{intentos}")
    numero_usuario = int(input("Introduce un número: "))
    
    if  numero_usuario not in range(1,101):
        print("Incorrecto, recuerda que el número ha de estar entre 1-100")
    elif numero_usuario < num_aleatorio:
        print ("Mi número es mayor")
    elif numero_usuario > num_aleatorio:
        print ("Mi número es menor")
    else:
        print (f"Correcto!!! Has adivinado en {intentos} intentos.")
        break

if num_aleatorio != numero_usuario:
        print(f"Has agotado tu 8 intentos. El número secreto era {num_aleatorio}")   

