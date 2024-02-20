texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10] #EXTRAE DESDE EL 2 HASTA 10 SIN INCLUIRLO
print(fragmento)
fragmento = texto[2:] #EXTRAE DESDE EL 2 HASTA EL FINAL
print(fragmento)
fragmento = texto[:10] #EXTRAE DESDE EL PRINCIPIO HASTA 10 SIN INCLUIRLO
print(fragmento)
fragmento = texto[0:10:2] #COMIENZO, HASTA DONDE, CADA CUANTOS COGE 1
print(fragmento)
fragmento = texto[::3] #DESDE EL PRIMERO HASTA EL ÚLTIMO COGIENDO 1 CADA 3
print(fragmento)
fragmento = texto[::-3] #DESDE EL ULTIMO HASTA EL PRIMERO COGIENDO 1 CADA 3
print(fragmento)
fragmento = texto[::-1] #DE ESTA FORMA INVERTIRIAMOS LA CADENA
print(fragmento)


