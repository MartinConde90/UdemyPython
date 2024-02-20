x = 10
y = 5

print("Mis numeros son " + str(x) + " y " + str(y))
print("--------------------------------------")

#VAMOS A HACERLO CON "FORMAT"
print("Mis numeros son {} y {}".format(x,y))
print("La suma de {} y {} es igual a {}".format(x,y,x+y))
print("--------------------------------------")

#OTRA FORMA DE PONER EL "FORMAT"
print(f"Mis numeros son {x} y {y}")
print(f"La suma de {x} y {y} es igual a {x+y}")
print("--------------------------------------")


color_coche = "verde"
matricula = 2013

print(f"El coche es de color {color_coche} y su matricula es {matricula}")