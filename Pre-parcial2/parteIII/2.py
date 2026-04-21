# 8. Dada la lista:
# numeros = [10, 20, 30, 40, 50]
# Desempaqueta:
# Primer número
# Último número
# Los intermedios usando *

palabras = []

for palabra in range(5):
    palabra = input("ingresa la palabra: ")
    palabras.append(palabra)

palabras = tuple(palabras)

palabraPrimero, *palabraIntermedio, palabraFinal = palabras

print(palabraPrimero)
print(palabraIntermedio)
print(palabraFinal)

