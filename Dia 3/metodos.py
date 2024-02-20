texto = "Este es el texto de Martin"
resultado = texto
print(resultado)
print("----------------------")
resultado = texto[3:20].upper()#SELECCION A MAYUSCULAS
print(resultado)
print("----------------------")
resultado = texto.lower()#TODO A MINUSCULAS
print(resultado)
print("----------------------")
resultado = texto.split()#DIVIDE POR COMAS DONDE ENCUENTRE VACIO
print(resultado)
resultado = texto.split("t")#DIVIDE POR COMAS DONDE ENCUENTRE "t"
print(resultado)
print("----------------------")


a = "Aprender"
b = "Python"
c = "es"
d = "genial"
lista = [a,b,c,d]
e = " ".join(lista)#UNE LOS DATOS DE LA LISTA POR ESPACIOS
print(e)
print("----------------------")

resultado = texto.find("texto")#DEVUELVE LA POSICION, SI NO EXISTE, DEVUELVE -1
print(resultado)
print("----------------------")

resultado = texto.replace("Martin", "Brandon")
print(resultado)
resultado = texto.replace("e", "i")
print(resultado)