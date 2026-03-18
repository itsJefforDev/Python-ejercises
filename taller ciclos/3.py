# Ejercicio 3 – Saltar números (continue)
# Crear un programa que imprima los números del 1 al 10, pero no debe 
# mostrar el número 5.
# Debe usar continue.


count = 0

while (count<=10):
    count += 1
    if(count ==5):
        continue
    print(count)