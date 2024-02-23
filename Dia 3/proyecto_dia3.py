#pedir al usuario que ingrese un texto
texto = input('Introduce un texto:').lower()

#pedir que ingrese 3 letras 
i = 0
letras = []
while i < 3:   
    letras.append(input('Introduce una letra:').lower())
    i +=1

#cuantas veces aparece cada letra en el texto
i = 0
for i in range(len(letras)):
    print(f'La letra {letras[i]} aparece: {texto.count(letras[i])} veces')

#cuantas palabras hay en el texto
palabras = texto.split()
print(f'El texto contiene {len(palabras)} palabras')

#primera y ultima letra del texto
print(f'La primera letra del texto es "{texto[0]}" y la última es "{texto[-1]}"')

#invertir el texto
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(texto_invertido)

#buscar la palabra 'python' en el texto
buscar = 'Python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra \'python\' {dic[buscar]} aparece en el texto")

