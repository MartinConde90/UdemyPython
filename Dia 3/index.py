mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a") #muestra la posición de la primera "a" que encuentre
print(resultado)
print("----------------------")
resultado = mi_texto.index("a",5) #muestra la posición de la primera "a" que encuentre a partir de la posicion 5
print(resultado)
print("----------------------")
resultado = mi_texto.index("a",5,11) #muestra la posición de la primera "a" que encuentre entre las posiciones 
print(resultado)                     #5 a 11 no incluida
print("----------------------")
resultado = mi_texto.rindex("a") #muestra la posición de la primera "a" que encuentre comenzando por la derecha
print(resultado)