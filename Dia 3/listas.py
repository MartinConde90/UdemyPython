print("1----------------------")
mi_lista = ['a','b','c']
print(type(mi_lista))

print("2----------------------")
resultado = len(mi_lista)
print(resultado)

print("3----------------------")
resultado = mi_lista[0:]
print(resultado)

print("4----------------------")
resultado = mi_lista[0:1] #HASTA EL 1, SIN COGERLO
print(resultado)

print("5----------------------")
otra_lista = ['hola',55,6.1]
print(type(otra_lista))

print("6----------------------")
mi_lista2 = ['d','e','f']
print(mi_lista+mi_lista2)

print("7----------------------")
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

print("8----------------------")
mi_lista3[0] = 'alfa'
print(mi_lista3)

print("9----------------------")
mi_lista3.append('g') #AÑADE AL FINAL
print(mi_lista3)

print("10----------------------")
mi_lista3.insert(2,"Ocelote")
print(mi_lista3)

print("11---------------------")
eliminado = mi_lista3.pop()#SI LO DEJAS VACÍO ELIMINA EL ÚLTIMO
print(mi_lista3)
print(eliminado)

print("12---------------------")
lista = ['g','o','b','m','c']
print(lista)
lista.sort()
# nueva_lista = lista.sort() ESTO NO SE PUEDE HACER
nueva_lista = lista # ASI SÍ
print(lista)
print(nueva_lista)

print("13---------------------")
lista.reverse()
print(lista)

