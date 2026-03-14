
#Ciclo for para recorrer una lista

# frutas = ["manzana", "pera", "uva"]

# for fruta in frutas:
#     print(fruta)

#Existe en todos los lenguajes de programcion
#En python no se piensa en contadores sino para 

# text = "jefferson"
#0 --> empieza en 0
#3 --> va hasta 3
#2 --> suma en dos en dos
# for i in range(0,3,2):
#     print(text)


precios = {"pan":2000,"uvas":5000}

for producto in precios:
    print(producto)

for producto in precios.values:
    print(producto)
