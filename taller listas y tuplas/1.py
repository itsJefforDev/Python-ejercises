# 1. Crear y mostrar lista
# Pídele al usuario 5 números y guárdalos en una lista.
# Muestra la lista completa.

numeros = []

for num in range(5):
    num = int(input("ingresa el numero: "))
    numeros.append(num)

print(numeros)

