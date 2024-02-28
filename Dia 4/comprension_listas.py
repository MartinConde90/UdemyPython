palabra = 'python'

#ANTERIOR FORMA DE HACERLO
lista = []
for letra in palabra:
    lista.append(letra)
print(lista) 

print('-----------------------------')
#CON COMPRENSION DE LISTAS
lista = [letra for letra in 'python']# Agrega una letra por cada letra que encuentres en 'python'
print(lista)

print('-----------------------------')
lista = [n for n in range(0,21,2)]
print(lista)
lista = [n / 2 for n in range(0,21,2)]
print(lista)
lista = [n for n in range(0,21,2) if n * 2 > 10]
print(lista)
lista = [n if n * 2 > 10 else 'n*2 es menor de 10' for n in range(0,21,2)]
print(lista)

print('---Pies a metros---')
pies = [10,20,30,40,50]
metros = [n/3.281 for n in pies]
print(metros)

print('---Pies a metros---')
pies = [10,20,30,40,50]
metros = [n*0.3048 for n in pies]
print(metros)
