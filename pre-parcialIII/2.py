palabras = []

for palabra in range(4):
    palabra = input("ingresa la palabra: ")
    palabras.append(palabra)

palabras = tuple(palabras)

palabraPrimero, *palabraIntermedio, palabraFinal = palabras

print(palabraPrimero)
print(palabraIntermedio)
print(palabraFinal)