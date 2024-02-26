monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No me quedan monedas")

print('-------------------------')

respuesta = 's'
while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n)")
    print('Continuemos!!!')
else:
    print("Hasta luego!!!")


print('-------------------------')
while respuesta == 's':
    pass

