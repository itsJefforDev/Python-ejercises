numeros = []

for i in range(6):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

cantidad = {}

for num in numeros:
    if num in cantidad:
        cantidad[num] += 1
    else:
        cantidad[num] = 1

print("diccionario", cantidad)
