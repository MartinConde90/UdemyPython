#COMBINACION DE LISTAS, ZIP LLEGA HASTA EL LARGO DE LA LISTA MAS CORTA

nombres = ['Ana','Hugo','Valeria','Paco']
edades = [65,29,42,55]
ciudades = ['Lima','Ourense','Mexico']

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")




