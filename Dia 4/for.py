print('1--Recorremos lista y mostramos su contenido')
lista = ['a','b','c']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: " + letra)

print('2--Recorremos lista y mostramos su contenido si cumple la condicion')
lista = ['pablo', 'laura', 'fede', 'luis', 'julia']
for nombre in lista:
    if nombre.startswith('l'):
        print('Nombre que comienza con L -> ' + nombre)
    else:
        print('Nombre que no comienza con L -> ' + nombre)

print('3--Recorremos lista y añadimos el valor de cada elemento a una variable')
numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

print('4--Recorremos string y mostramos cada caracter')
palabra = 'python'
for letra in palabra:
    print(letra)

print('5--Recorremos string y mostramos cada caracter, esta vez introduciendo el string directamente en el bucle')
for letra in 'python':
    print(letra)

print('6--Recorremos lista anidada')
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print('7--Recorremos diccionario')
dic = {'clave1':'a','clave2':'b','clave3':'c'}
for item in dic.values():
    print(item)

for x,y in dic.items():
    print(x,y)

print('8--BREAK')
nombre = input('Ingresa tu nombre: ')
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

print('9--CONTINUE')
nombre = input('Ingresa tu nombre: ')
for letra in nombre:
    if letra == 'r':
        continue
    print(letra) 