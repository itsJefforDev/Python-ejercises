# Listas y bucles (0.625)
# Pida al usuario 6 números y guárdelos en una lista.
# Luego:
# Muestre la lista
# Muestre la suma total usando un for


numeros = []
resultado = 0

for num in range(6):
    num = int(input("ingresa el numero: "))
    resultado = resultado + num
    numeros.append(num)

print(numeros)
print(resultado)