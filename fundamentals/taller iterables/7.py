text = input("Por favor ingrese una frase: ")

count = 0

for i in text:
    if i.isupper():
        count += 1

print(count)