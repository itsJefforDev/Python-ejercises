# 8. Dada la lista:
# numeros = [10, 20, 30, 40, 50]
# Desempaqueta:
# Primer número
# Último número
# Los intermedios usando *

numeros = [10, 20, 30, 40, 50]

numPrimero, *numIntermedio, numFinal = numeros

print(numPrimero)
print(numIntermedio)
print(numFinal)

