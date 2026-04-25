# Diccionario principal donde se almacenan los usuarios
# La clave será el ID del usuario y el valor otro diccionario con sus datos
usuarios = {}

####CREATE
def crear_usuario(id, nombre, edad):
    # Verifica si el ID ya existe en el diccionario
    if id in usuarios:
        print("El usuario ya existe")
    else:
        # Si no existe, crea un nuevo usuario como diccionario
        usuarios[id] = {
            "nombre": nombre,
            "edad": edad
        }
        print("Usuario creado")


###READ

def leer_usuarios():
    # Verifica si el diccionario está vacío
    if not usuarios:
        print("No hay usuarios")
    else:
        # Recorre todos los usuarios
        for id, datos in usuarios.items():
            # Imprime cada usuario con sus datos
            print(f"ID: {id} | Nombre: {datos['nombre']} | Edad: {datos['edad']}")


def leer_usuario(id):
    # Verifica si el usuario existe
    if id in usuarios:
        # Muestra la información del usuario
        print(usuarios[id])
    else:
        print("Usuario no encontrado")


###UPDATE

def actualizar_usuario(id, nombre=None, edad=None):
    # Verifica si el usuario existe
    if id in usuarios:
        # Si se proporciona un nuevo nombre, se actualiza
        if nombre:
            usuarios[id]["nombre"] = nombre
        
        # Si se proporciona una nueva edad, se actualiza
        if edad:
            usuarios[id]["edad"] = edad
        
        print("Usuario actualizado")
    else:
        print("Usuario no encontrado")

###DELETE
def eliminar_usuario(id):
    # Verifica si el usuario existe
    if id in usuarios:
        # Elimina el usuario del diccionario
        del usuarios[id]
        print("Usuario eliminado")
    else:
        print("Usuario no encontrado")

########Ejemplo de uso
# Crear usuarios
crear_usuario(1, "Ana", 25)
crear_usuario(2, "Luis", 30)

# Mostrar todos los usuarios
leer_usuarios()

# Actualizar la edad del usuario con ID 1
actualizar_usuario(1, edad=26)

# Mostrar un solo usuario
leer_usuario(1)

# Eliminar un usuario
eliminar_usuario(2)

# Mostrar usuarios después de eliminar
leer_usuarios()


