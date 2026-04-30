
dic1 = {}

for i in range(4):
    clave = input(f"Ingrese la clave: ")
    valor = input(f"Ingrese el valor de: ")
    dic1[clave] = valor

dic2 = {}

for clave, valor in dic1.items():
    dic2[valor] = clave

print("Diccionario 1:")
print(dic1)

print("Diccionario 2:")
print(dic2)
