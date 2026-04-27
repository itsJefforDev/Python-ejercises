empleados = {}

for i in range(2):
    nombre = input(f"nombre del empleado {i+1}: ")
    cargo = input(f"cargo del empleado {i+1}: ")
    salario = float(input("salario: "))
    
    empleados[i] = {
        "nombre": nombre,
        "cargo": cargo,
        "salario": salario
    }

for nombreEmpleado in empleados.values():
    print(nombreEmpleado["nombre"])

mayorSalario = 0
nombreMayor = ""

for empleado in empleados.values():
    if empleado["salario"] > mayorSalario:
        mayorSalario = empleado["salario"]
        nombreMayor = empleado["nombre"]

print("empleado con mayor salario:")
print(nombreMayor, "con salario de", mayorSalario)