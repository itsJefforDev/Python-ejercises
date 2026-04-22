numeros = []
for num in range(6):
    num = int(input("ingresa el numero: "))
    numeros.append(num)
print(numeros)

numeros = tuple(numeros)
print(numeros)

numeros = set(numeros)
print(numeros)

numPrimero, *_, numFinal = numeros
print(numPrimero,numFinal)

_,*intermedios,_ = numeros
print(intermedios)


counter = 0
for num in numeros:
    counter += 1

print("Elementos unicos: ",counter)