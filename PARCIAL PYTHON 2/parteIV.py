# PARTE IV – EJERCICIO INTEGRADOR (1.0)
# Realizar en Visual Studio o IDLE.
# Pida al usuario 6 números.
# Luego:
# Guárdelos en una lista
# Convierta la lista en tupla
# Desempaque el primero y el último
# Guarde los intermedios
# Convierta los números a conjunto

# Muestre:
# La lista
# La tupla
# Primer número
# Último número
# Intermedios
# Cantidad de elementos únicos

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