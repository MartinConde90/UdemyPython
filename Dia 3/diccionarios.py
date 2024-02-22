print("1-Mostramos contenido de diccionario")
diccionario = {'c1':'valor1',
               'c2':'valor2'}
print(diccionario)

print("2-Mostramos contenido de la clave 'c1'")
resultado = diccionario['c1']
print(resultado)

print("3-Mostramos el contenido de apellido")
cliente = {'nombre':'Juan', 'apellido':'Fuentes','peso':88,'talla':1.75}
print(cliente)
consulta = cliente['apellido']
print(consulta)

print("4-Mostramos contenido de c2, que es una lista y despues de c3, que tambien es un diccionario")
dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic)
print(dic['c2'][1])
print(dic['c3']['s2'])

print("5-Mostrar contenido del segundo elemento de 'c2' pero en mayúscula ")
dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic2)
print(dic2['c2'][1].upper())

print("6-Introducimos un nuevo elemento en el diccionario y luego añadimos otro pero sobreescribiendo uno existente")
dic3 = {1:'a',2:'b'}
print(dic3)
dic3[3] = 'c'
print(dic3)
dic3[2] = 'B'
print(dic3)

print("7-Mostramos las claves de dic3, despues los valores y al final todo")
print(dic3)
print(dic3.keys())
print(dic3.values())
print(dic3.items())