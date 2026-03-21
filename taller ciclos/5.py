# Ejercicio 5 – Adivinar número (while + break)
# Definir un número secreto: .
# Pedir al usuario que adivine el número.
# Si es incorrecto, seguir preguntando.
# Cuando lo adivine mostrar: "Correcto, adivinaste el número".


secretNumber = 6

while True:
    inputUser = int(input("Escribe un numero para adivinar: "))
    
    if(inputUser==secretNumber):
        print("Adivinaste!")
        break
    else:
        print("Sigue intentando")
