
secretNumber = 6

while True:
    inputUser = int(input("Escribe un numero para adivinar: "))
    
    if(inputUser==secretNumber):
        print("Adivinaste!")
        break
    else:
        print("Sigue intentando")
