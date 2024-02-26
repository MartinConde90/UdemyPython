#ACCEDER DE FORMA SENCILLA A LOS INDICES DE UN OBJETO ITERABLE
lista = ['a','b','c']
indice = 0

for item in enumerate(lista):
    print(item)
print('-------------------')

for indice,item in enumerate(lista):
    print(indice,item)
print('-------------------')

for item in enumerate(range(50,55)):
    print(item)

print('-------------------')
for indice,item in enumerate(range(50,55)):
    print(indice,item)

print('-------------------')
mis_tuples = list(enumerate(lista))
print(mis_tuples)