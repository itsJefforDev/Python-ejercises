
#Definimos variables para validar el login
# usuario = "admin"
# contraseña = "python123"

#Definimos los inputs para que el usuario pueda ingresar datos
# inputUser = input("Por favor ingrese su usuario: ")
# inputPass = input("Por favor ingrse su contraseña: ")


#Proceso de validacion del login
##Primero validamos el usuario y despues la contraseña
###En caso de no coincidir alguno de los dos arroja su mensaje de error

# if(inputUser==usuario):
#     if(inputPass==contraseña):
#         print("Acceso correcto bienvenido :)",usuario)
#     else:
#         print("Contraseña incorrecta")
# else:
#     print("usuario incorrecto")


####Validar si un numero es par o impar

#Creamos el input para que el usuario ingrese un numero
# inputNumber = int(input("Por favor ingrese un numero: "))


#Validamos con una con una condicional si es par o impar
##Primero necesitamos saber si el modulo del numero ingresado es 0
###Si el modulo o el residuo de ese numero es 0, quiere decir que se puede
###dividir entre dos, es decir son numeros pares
# if(inputNumber %2 == 0):
#     print("El numero",inputNumber,"es PAR")
# else:
#     print("El numero",inputNumber,"es IMPAR")


####Verificacion de color

#Creamos el input para que el usuario ingrese un color
# inputColor = input("Por favor ingrese su color favorito: ")

#Validamos con una con una condicional si es azul o no
# if(inputColor=="azul"):
#     print("Buen gusto")
# else:
#     print("Interesante eleccion")


####Dias de la semana

###creamos una entradad para el usuario
inputDia = input("Digite un dia: ")

##Creamos un match para poder validar los dias de la semana
###Esta funcion tambien valida si ingresa un dia que no corresponde
match(inputDia):
    case "sabado":
        print("Es fin de semana")
    case "domingo":
        print("Es fin de semana")
    case "viernes":
        print("Ya casi es fin de semana")
    case "lunes":
        print("Es dia de estudio")
    case "martes":
        print("Es dia de estudio")
    case "miercoles":
        print("Es dia de estudio")
    case "jueves":
        print("Es dia de estudio")
    case default:
        print("Digite un dia valido")
