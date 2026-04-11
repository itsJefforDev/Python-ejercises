# 4. Lista → Tupla
# Pídele al usuario 4 números y guárdalos en una lista.
# Convierte esa lista en tupla y muéstrala.

numeros = []

for num in range(4):
    num = int(input("ingresa el numero: "))
    numeros.append(num)

numeros = tuple(numeros)
print(numeros)
