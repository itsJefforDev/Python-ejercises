productos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    productos[nombre] = precio


print("Productos con precio mayor a 50:")
for nombre, precio in productos.items():
    if precio > 50:
        print(nombre, ":", precio)
