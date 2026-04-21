# Conjuntos (0.625)
# Pida al usuario 6 números (pueden repetirse).
# Guárdelos en un conjunto y luego:
# Muestre el conjunto
# Muestre cuántos elementos únicos tiene

numeros = []

for num in range(6):
    num = int(input("ingresa el numero: "))
    numeros.append(num)

numeros = set(numeros)
print(numeros)