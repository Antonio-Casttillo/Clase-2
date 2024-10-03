#Hecho por antonio, rafael y jossemir

import random

#Damos nombre a la clase
class Empleado:
    #una funcion para alamacenar los datos
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.id = self.generar_id()
        self.locker = self.generar_locker()
        self.sistema = self.asigna_sistema()
        self.nip = None

        #funcion que genera un codigo con 10 numeros aleatorios del 1 al 9
    def generar_id(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(10))

        #funcion que genera un codigo con 2 numeros aleatorios del 1 al 9
    def generar_locker(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(2))

        # una funcion que elige aleatoriamente entre la opcion Escolarizado o Sabatino utilizando una variable bulean
    def asigna_sistema(self):
        asignar_sistema = random.randint(1, 2)
        return "Escolarizado" if asignar_sistema == 1 else "Sabatino"


        #va a retornar las funciones antes mencionadas para mostrarlas
    def __str__(self):
        return (f"Alumno: {self.nombre} {self.apellido}\n"
                f"Numero de registro: {self.id}\n"
                f"Locker No.: {self.locker}\n"
                f"Turno asignado: {self.sistema}")

#esta linea muestra las siguientes dos lienas entre comillas en la pantalla
def main():
    print("Bienvenido al Instituto Tecnologico Superior de Martínez de la Torre.\n")
    print("Ingrese los siguientes campos que se le solicitan: \n")

# se pide al usuario que ingrese los siguientes parametros
    nombre_ar = input("Nombre: ")
    apellido_ar = input("Apellido: ")
    nip = input("Digite su Matricula: ")

#almacena los datos y los guarda en la variable "empleado1"
    empleado1 = Empleado(nombre_ar, apellido_ar)
    empleado1.nip = nip

    print(empleado1)

#crea un metodo para dirigir el codigo de la linea 38
if __name__ == "__main__":
    main()
