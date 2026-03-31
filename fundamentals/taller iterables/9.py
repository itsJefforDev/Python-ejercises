#     9. Mostrar caracteres uno por uno  
# Pídele al usuario una frase. 
# Muestra cada carácter en una línea, incluyendo espacios. 
 
text = input("Ingresa una palabra: ")

iterador = iter(text)

for i in iterador:
    print(i)