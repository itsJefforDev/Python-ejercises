#realizar un algoritmo que valide 3 numero y determite cual
#de los 3 es el mayor

number1 = input('digite el numero 1: ')
number2 = input('digite el numero 2: ')
number3 = input('digite el numero 3: ')

if(number1 > number2):
    if(number1>number3):
        print('el numero ',number1,' es el mayor')
    elif(number3>number2):
        print('el numero ',number3,' es el mayor')
    else:
        print('los tres numero son iguales') 
elif(number2>number3):
    print('el numero ',number2,' es mayor')
else:
    print('el numero ',number3,' es mayor')