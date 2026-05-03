

inventario = set()

def crearProducto():

    producto = input("ingrese el nombre del producto: ")

    inventario.add(producto)
    print(f"producto {producto} agregado")


def leerProductos():

    print("\ninventario actual:")
    print(inventario)


def actualizarProducto():

    productoBuscado = input("ingrese el producto a actualizar: ")

    if productoBuscado not in inventario:
        print("el producto no existe")
        return

    productoActualizado = input("ingrese el nuevo nombre: ")

    inventario.remove(productoBuscado)
    inventario.add(productoActualizado)

    print(f"el producto {productoBuscado} actualizado a {productoActualizado}")


def eliminarProducto():

    producto = input("Ingrese el producto a eliminar: ")

    if producto in inventario:
        inventario.discard(producto)
        print(f"producto {producto} eliminado")



def eliminarTodo():

        inventario.clear()
        print("inventario eliminado")



def buscarProducto():

    producto = input("ingrese el producto para buscarlo: ")

    if producto in inventario:
        print(f"{producto} si esta en el inventario")
    else:
        print(f"{producto} si esta en el inventario")


while True:
    print("MENÚ INVENTARIO")
    print("1. crear producto")
    print("2. ver inventario")
    print("3. actualizar producto")
    print("4. eliminar producto")
    print("5. buscar producto")
    print("6. borrar inventario")
    print("7. salir")

    inputUserOption = input("seleccione una opción: ")

    inputUserOption = int(inputUserOption)

    match inputUserOption:
        case 1:
            crearProducto()
        case 2:
            leerProductos()
        case 3:
            actualizarProducto()
        case 4:
            eliminarProducto()
        case 5:
            buscarProducto()
        case 6:
            eliminarTodo()
        case 7:
            break
        case _:
            print("opcion no valida")

