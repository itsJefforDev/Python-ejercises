
factura = (
    1,
    "Carlos Pérez",
    [
        ("Laptop", 1, 2500),
        ("Mouse", 2, 100),
        ("Teclado", 1, 150)
    ],
    2850
)

id_factura = factura[0]
cliente = factura[1]
productos = factura[2]
totalRegistrado = factura[3]

print("FACTURA")
print(f"ID: {id_factura}")
print(f"Cliente: {cliente}")
print("\nProductos:\n")

totalCalculado = 0

for nombre, cantidad, precio in productos:
    
    subtotal = cantidad * precio
    totalCalculado += subtotal

    print(f"Producto: {nombre}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: ${precio}")
    print(f"Subtotal: ${subtotal}")

print(f"Total registrado: ${totalRegistrado}")
print(f"Total calculado: ${totalCalculado}")


if totalCalculado == totalRegistrado:
    print("Factura consistente")
else:
    print("Factura alterada")