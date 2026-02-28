# class → define la clase
# __init__ → constructor (se ejecuta al crear el objeto)
# self → representa la instancia actual
# Métodos → funciones dentro de la clase


class NombreDeLaClase:
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2

    def metodo(self):
        print(f"Hola, soy {self.parametro1} y tengo {self.parametro2}")

nombreDeLaClase = NombreDeLaClase("jeff",24)
nombreDeLaClase.metodo()