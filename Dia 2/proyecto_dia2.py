nombre = input("Introduce tu nombre:")
ventas = int(input("Introduce tus ventas mensuales:"))

comision = round(ventas*13/100,2)

print(f"Hola {nombre}!. Este mes ganaste {comision}€ en comisiones")