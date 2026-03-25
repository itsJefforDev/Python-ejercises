#     8. zip con palabra  
# Pídele al usuario una palabra. 
# Crea una lista de números desde 1 hasta la longitud de la palabra. 
# Luego usa zip() para emparejar cada número con una letra. 
# Usa zip() para mostrar: 
# 1 - p 
# 2 - y 
# 3 – t 

text = input("Ingresa una palabra: ")

numeros = list(range(1, len(text) + 1))

finalList = zip(numeros, text)

for numero, letra in finalList:
    print(numero, letra)
