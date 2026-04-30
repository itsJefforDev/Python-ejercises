palabra = input("ingrese una palabra para validar: ")

cantidad = {}

for letra in palabra:
    if letra in cantidad:
        cantidad[letra] += 1
    else:
        cantidad[letra] = 1

print(cantidad)

