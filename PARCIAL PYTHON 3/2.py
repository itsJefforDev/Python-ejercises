
estudiante = {
    "nombre": "Chroma",
    "carrera": "Secretariado",
    "creditos": 3,
    "estado": "activo",
    "promedio": 4.1
}

print(f"diccionario original: {estudiante}")

estudiante["creditos"] += 12


if estudiante["promedio"] >= 4.0:
    estudiante["estado"] = "graduado"


del estudiante["carrera"]


for llave, valor in estudiante.items():
    print(f"{llave}: {valor}")