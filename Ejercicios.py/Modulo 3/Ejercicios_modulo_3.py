# Ejercicios Modulo 3:

# 1º Se ha definido una clase relativa al inventario de jet imaginario.
# También se ha creado una instancia de esta clase Jet. 
# Imprime el primer atributo de la instancia.

class Jet:
    def __init__(self, modelo, nacionalidad):
        self.modelo = modelo
        self.nacionalidad = nacionalidad

mi_jet = Jet("F-16", "USA")

print(mi_jet.modelo)

# 2º Usando la clase Jet, crea nuevas instancias con los siguientes nombres y orígenes:
# SU33: Russia
# AJS37: Sweden
# Mirage2000: France
# F14: USA
# Mig29: USSR
# A10: USA

class Jet:
    def __init__(self, modelo, nacionalidad):
        self.modelo = modelo
        self.nacionalidad = nacionalidad

    def info_basica(self):
        print(f"Modelo: {self.modelo}, Nacionalidad: {self.nacionalidad}")

su33 = Jet("SU33", "Russia")
ajs37 = Jet("AJS37", "Sweden")
mirage2000 = Jet("Mirage2000", "France")
f14 = Jet("F14", "USA")
mig29 = Jet("Mig29", "USSR")
a10 = Jet("A10", "USA")

su33.info_basica() 
ajs37.info_basica()
mirage2000.info_basica()
f14.info_basica()
mig29.info_basica()
a10.info_basica()

# 3º Añade otro atributo llamado "cantidad" a la clase.
# El usuario le dara valor pasando un nuevo parámetro por el constructor. 
# A continuación crear 2 instancias para: F14 y Mirage2000 con las cantidades 87 y 35

class Jet:
    def __init__(self, modelo, nacionalidad, cantidad):
        self.modelo = modelo
        self.nacionalidad = nacionalidad
        self.cantidad = cantidad
    def info_basica(self):
        print(f"Modelo: {self.modelo}, Nacionalidad: {self.nacionalidad}, Cantidad: {self.cantidad}")

f14 = Jet("F14", "USA", 87)
mirage2000 = Jet("Mirage2000", "France", 35)

f14.info_basica()
mirage2000.info_basica()

# 4º Dada la siguiente instancia y sus atributos, crea una clase que la instancie.

# np2005 = Nobel("Peace", 2005, "Muhamad Yunus")
# print(np2005.category, np2005.year, np2005.winner)

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

np2005 = Nobel("Peace", 2005, "Muhamad Yunus")

print(np2005.category, np2005.year, np2005.winner)

# 5º Crea una clase con el nombre de Estudiante, e inicialice 
# atributos como el nombre, la edad y el grado mientras crea un objeto. 

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

alumno = Estudiante("Juan", 13, "3º ESO")

print(alumno.nombre, alumno.edad, alumno.grado)

# 6º Escribe un programa para crear una clase vacía válida con el nombre de 
# Estudiante, sin propiedades. 

class Estudiante: 
    pass

# 7º Añade un método público en la clase Estudiante que calcule la media de lista 
# de notas y actuualice el valor del atributo grade. a continuación llama a 
# la función en tu grograma principal e imprime el valor de grade.

class Estudiante:
    def __init__(self):
      self.grade = 0
    def media(self, notas: list):
        if notas:
            self.grade = sum(notas)/ len(notas)
        else: 
            self.grade = 0


notas_juan = [10, 8, 9, 5, 6, 7]
juan = Estudiante()

juan.media(notas_juan)

print(f"Media: {juan.grade}")

# 8º Añade a la clase anterior, un método estático que dada una lista de notas
# y sus asignaturas asociadas como diccionarios, imprima aquellas asignaturas
# que han recibido una nota inferior a 5. 

class Estudiante:
    def __init__(self):
      self.grade = 0
    def media(self, notas):
        if notas:
            self.grade = sum(notas)/ len(notas)
        else: 
            self.grade = 0

    @staticmethod
    def suspensos(notas_por_asignatura):
        print("Asignaturas suspendidas")
        for asignatura, nota in notas_por_asignatura.items():
            if nota < 5:
                print(f"{asignatura} : {nota}")

notas_estudiante = [10, 8, 9, 5, 4, 7]
notas_por_asignatura = {"Matematicas": 10,
                        "Ingles": 8,
                        "Física": 9,
                        "Lengua": 5,
                        "Química": 4,
                        "Arte": 7}

alumno = Estudiante()

alumno.media(notas_estudiante)
alumno.suspensos(notas_por_asignatura)

# 9º Añade un atributo de clase llamado escuela a la clase Estudiante y 
# dale un valor predeterminado. A continuación, añade un método de clase que 
# dado el nombre de otra escuela actualice el valor de este atributo. 
# Llama a tu método en el programa principal y asegúrate de que funcione. 

class Estudiante:
    escuela = "Escuela Musk"
    def __init__(self):
      self.grade = 0
    def media(self, notas):
        if notas:
            self.grade = sum(notas)/ len(notas)
        else: 
            self.grade = 0

    @staticmethod
    def suspensos(notas_por_asignatura):
        print("Asignaturas suspendidas")
        for asignatura, nota in notas_por_asignatura.items():
            if nota < 5:
                print(f"{asignatura} : {nota}")
    
    @classmethod
    def escuela_actual(cls, la_escuela):
        cls.escuela = la_escuela
        print(cls.escuela)
    
notas_estudiante = [10, 8, 9, 5, 4, 7]
notas_por_asignatura = {"Matematicas": 10,
                        "Ingles": 8,
                        "Física": 9,
                        "Lengua": 5,
                        "Química": 4,
                        "Arte": 7}

alumno = Estudiante()

alumno.media(notas_estudiante)
alumno.suspensos(notas_por_asignatura)
alumno.escuela_actual("Musk")

# 10º Añade un método privado en la clase anterior, que dado un diccionario mes-número 
# de asistencias, devuelva 1 si algún mes tiene una asignatura < 4, 
# duvuelva 2 si algún mes tiene alguna asistencia entre [4, 8] o bien devuelva 3 en caso contrario.
# Para probar el método privado, encapsúlalo con una función pública que devuelva su resultado. 


class Estudiante:
    escuela = "Escuela Musk"
    def __init__(self):
      self.grade = 0
    
    def media(self, notas):
        if notas:
            self.grade = sum(notas)/ len(notas)
        else: 
            self.grade = 0

    @staticmethod
    def suspensos(notas_por_asignatura):
        print("Asignaturas suspendidas")
        for asignatura, nota in notas_por_asignatura.items():
            if nota < 5:
                print(f"{asignatura} : {nota}")
    
    @classmethod
    def escuela_actual(cls, la_escuela):
        cls.escuela = la_escuela
        print(cls.escuela)
    
    def calcular_asistencias(self,asistencias):
        for mes,asistencia in asistencias.items():
            if asistencia < 4:
                return 1
            elif 4 <= asistencia <= 8:
                return 2
        return 3
    
    def asistencias_finales(self,asistencias):
        return self.calcular_asistencias(asistencias)
    
notas_estudiante = [10, 8, 9, 5, 4, 7]
notas_por_asignatura = {"Matematicas": 10,
                        "Ingles": 8,
                        "Física": 9,
                        "Lengua": 5,
                        "Química": 4,
                        "Arte": 7}

asistencias_mes = {"Enero": 1,
                   "Febrero": 9,
                   "Marzo": 3,
                   "Abril": 7,
                   "Mayo": 10}

alumno = Estudiante()
asistencias = alumno.asistencias_finales(asistencias_mes)

alumno.media(notas_estudiante)
alumno.suspensos(notas_por_asignatura)
alumno.escuela_actual("Musk")
print(f"Asistencia: {asistencias}")