#     12. Conjuntos de materias inscritas 
 
# Dos estudiantes inscribieron materias. 
 
# juan = {"Bases de datos", "Python", "Inglés", "Estadística"} 
# ana = {"Python", "Diseño UX", "Estadística", "Cálculo"} 
 
# Haz lo siguiente: 
 
# Muestra las materias que tienen en común. 
# Muestra las materias que solo ve Juan. 
# Muestra las materias que solo ve Ana. 
# Muestra todas las materias entre ambos sin repetir.


# Conjuntos de materias
juan = {"Bases de datos", "Python", "Inglés", "Estadística"}
ana = {"Python", "Diseño UX", "Estadística", "Cálculo"}

# Materias en común
comunes = []
for materia in juan:
    if materia in ana:
        comunes.append(materia)

print("Materias en común:", comunes)

# Materias solo de Juan
solo_juan = []
for materia in juan:
    if materia not in ana:
        solo_juan.append(materia)

print("Materias solo de Juan:", solo_juan)

# Materias solo de Ana
solo_ana = []
for materia in ana:
    if materia not in juan:
        solo_ana.append(materia)

print("Materias solo de Ana:", solo_ana)

# Todas las materias sin repetir
todas = []

for materia in juan:
    if materia not in todas:
        todas.append(materia)

for materia in ana:
    if materia not in todas:
        todas.append(materia)

print("Todas las materias:", todas)