numeros = []

for num in range(6):
    num = int(input("ingresa el numero: "))
    numeros.append(num)

numeros2 = numeros
numeros2[0] = 7
print(numeros)