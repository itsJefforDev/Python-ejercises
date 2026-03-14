
#En Python no existe una estructura do...while nativa como en C, Java o JavaScript.
#Pero se puede simular usando un while True y un break.
#break interumpe el ciclo
#continue continua el ciclo sin romperlo

numero = 0

while True:
    numero = int(input("Ingresa un número mayor que 10: "))
    
    if numero > 10:
        break

print("Número válido:", numero)

