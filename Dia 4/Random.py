from random import *

print('1-Randint->Número entero aleatorio')
aleatorio = randint(1,50)
print(aleatorio)

print('2-Uniform->Número decimal aleatorio')
aleatorio = round(uniform(1,5),2)
print(aleatorio)

print('3-Random->Número aleatorio entre 0-1')
aleatorio = round(random(),2)
print(aleatorio)

print('4-Choice-> Elige aleatoriamente dentro de una lista')
colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

print('5-Shuffle-> Mezcla los elementos')
numero = list(range(0,50,5))
print(numero)
shuffle(numero)
print(numero)