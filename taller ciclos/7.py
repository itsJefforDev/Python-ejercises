# Ejercicio 7 – Menú simple (while)
# Crear un programa que muestre el menú:
# 1. Saludar
# 2. Mostrar mensaje
# 3. Salir
# El programa debe repetirse usando while.
# Si el usuario elige 1   mostrar "Hola usuario"→
# Si elige 2   mostrar "Aprendiendo Python"→
# Si elige 3   terminar el programa usando break.→

secretNumber = 6

while True:

    print("1. Saludar\n" \
    "2. Mostrar mensaje\n" \
    "3. Salir\n")
    inputUser = int(input("Elige una opcion "))
    
    match (inputUser):
        case 1:
            print("hola usuario")
            continue
        case 2:
            print("Aprendiendo python")
            continue
        case 3:
            break
        case default:
            print("Numero incorrecto")
