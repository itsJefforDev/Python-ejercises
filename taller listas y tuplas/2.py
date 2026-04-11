# 2. Acceso por índice
# Pídele al usuario 4 palabras y guárdalas en una lista.
# Muestra:
# La primera
# La última

palabras = []

for palabra in range(4):
    palabra = input("ingresa la palabra: ")
    palabras.append(palabra)

print(palabras[0],palabras[-1])
