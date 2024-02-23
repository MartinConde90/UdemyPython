print('1-Mostramos el tipo de dato para comprobar que son tuplas aun inicializandolas de distintas formas')
mi_tuple = 1,2.5,3,4,'hello'
print(type(mi_tuple))
print(mi_tuple)
mi_tuple = (1,2,3,4,'hello')
print(type(mi_tuple))
print(mi_tuple[4])
mi_tuple = 'a','n','n'
print(type(mi_tuple))

print('2-Anidamiento--Mostramos la posicion 1 del tuple anidado en la posicion 2')
mi_tuple = (1,2,('a','b'),4,'hello')
print(mi_tuple[2][1])

print('3-Una lista con un tuple asignado, será una lista')
mi_tuple = list(mi_tuple)
print(type(list(mi_tuple)))

print('4-Mostramos como asignando el tuple a un numero de variables igual al numero de items de un tuple, metemos cada item en cada variable')
t = (1,2,3,1)
w,x,y,z = t
print(x,y,z)

print('5-Utilizamos el metodo \'count()\' para mostrar el numero de repeticiones del item que queramos')
print(t.count(1))

print('6-Utilizamos el metodo \'index()\' para mostrar el indice del item indicado')
print(t.index(2))