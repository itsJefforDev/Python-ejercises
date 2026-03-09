# class → define la clase
# __init__ → constructor (se ejecuta al crear el objeto)
# self → representa la instancia actual
# Métodos → funciones dentro de la clase


class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def createPerson(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad}")

nombreDeLaClase = Person("jeff",24)
nombreDeLaClase.createPerson()