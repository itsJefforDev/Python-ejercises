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
