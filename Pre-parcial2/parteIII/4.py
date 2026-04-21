# Tupla y acceso por índice (0.625)
# Pida al usuario 4 números y cree una tupla.
# Luego muestre:
# El primer número
# El último número

numeros = []

for num in range(4):
    num = int(input("ingresa el numero: "))
    numeros.append(num)

numeros = tuple(numeros)

numPrimero, *_, numFinal = numeros

print(numPrimero)
print(numFinal)
