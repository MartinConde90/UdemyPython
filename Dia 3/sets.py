
print('ORDENADOS NI NADA RELACIONADO CON SU POSICION ADEMÁS TAMBIÉN SON INMUTABLES')

print('1-set([1,2,3,4,5,6]), PONDREMOS [],{} O () DENTRO DE LOS () DEL PROPIO SET, EL CONTENIDO SE LEERÁ COMO UN ÚNICO ELEMENTO ')
mi_set = set([1,2,3,4,5])
print(mi_set)
print(type(mi_set))

print('2-{1,2,3,4,5,6}, DE ESTA FORMA NO HACE FALTA PONER [],{} O () A MAYORES')
otro_set = {1,2,3}
print(otro_set)
print(type(otro_set))

print('3-SUS ELEMENTOS NO PUEDEN SER INDEXADOS-> mi_set[0]')
try:
    mi_set[0]
except Exception as e: print(e)

print('4-LOS SETS NO PERMITEN ITEMS DUPLICADOS, SI APARECE UN DUPLICADO, LO ELIMINARÁ SIN PREGUNTAR-> set([1,2,3,4,2,3,4,1])')
new_set = set([1,2,3,4,2,3,4,1])
print(new_set)

print('5-NO ADMITEN LISTAS NI DICCIONARIOS-> new_set = set([1,[5,7],2])')
try:
    new_set = set([1,[5,7],2])
except Exception as e: print(e)

print('6-SI ADMITIRÁ TUPLES YA QUE ESTOS TAMBIÉN SON INMUTABLES')
new_set = set([1,(1,1),2,6,7,9,3])
print(new_set)
print(type(new_set))

print('7-MOSTRAMOS SI UN ELEMENTO SE ENCUENTRA EN EL SET')
print(2 in mi_set)

print('8-CREAMOS DOS SETS Y LOS UNIMOS EN UN TERCER SET')
s1 = set([1,2,3])
s2 = set([3,4,5])
s3 = s1.union(s2)
print(s3)

print('9-METODO \'add()\' PARA AGREGAR')
s3.add(6)
print(s3)

print('10-METODOS \'remove() y discard()\' PARA ELIMINAR')
s3.remove(6)
print(s3)
s3.discard(5)
print(s3)

print('11-METODO \'pop()\' ELIMINARÁ UN ELEMENTO ALEATORIO AL NO ESTAR INDEXADOS, SI NO LE INDICAMOS NADA')
s3.pop()
print(s3)

print('12-METODO \'clear()\' PARA VACIAR EL SET')
s3.clear()
print(s3)