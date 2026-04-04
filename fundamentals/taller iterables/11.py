#     11. Registro de datos inmutables  
 
# Crea una lista llamada estudiante con los siguientes datos: 
# Nombre, Código, Carrera, Promedio final, Estado de matrícula (True o 
# False) 
 
# Luego: 
# Muestra los datos de forma legible. 
# Verifica si el promedio es mayor o igual a 3.0 
# Si sí, mostrar “Estudiante aprobado” 
# Si no, “Estudiante reprobado”.

nombre = input("Ingrese su nombre: ")
codigo = input("Ingrese su codigo: ")
carrera = input("Ingrese su carrera: ")
promedioFinal = float(input("Ingrese su promedio final: "))
estadoDeMatricula = True


estudiante = [nombre,codigo,carrera, promedioFinal,estadoDeMatricula]

print("=== Datos del Estudiante ===")
print(f"Nombre: {estudiante[0]}")
print(f"Código: {estudiante[1]}")
print(f"Carrera: {estudiante[2]}")
print(f"Promedio final: {estudiante[3]}")
print(f"Estado de matrícula: {estudiante[4]}")

if(estudiante[3]>=3.0):
    print("Aprobado")
else:
    print("Reprobado")