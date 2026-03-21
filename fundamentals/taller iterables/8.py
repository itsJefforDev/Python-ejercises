text = input("Ingresa una palabra: ")

numeros = list(range(1, len(text) + 1))

finalList = zip(numeros, text)

for numero, letra in finalList:
    print(numero, letra)
