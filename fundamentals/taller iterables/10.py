#     10. Clasificar caracteres básico  
# Pídele al usuario una frase. 
# Muestra: 
# Cantidad de letras (solo caracteres alfabéticos) y Cantidad de espacios 

text = input("Ingresa una palabra: ")
countAlpha = 0
countBlank = 0

for i in text:
    if i.isalpha():
        countAlpha += 1
        continue
    else:
        countBlank += 1
        continue

print("Cantidad de alfabeticos: ",countAlpha)
print("Cantidad de espacios: ",countBlank)
    
