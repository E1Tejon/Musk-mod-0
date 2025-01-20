# EJERCICIOS MODULO 6:

# 1ª Crea una clase Staff con los atributos role, dept y salary.
# Crea una clase Profesor que herede de la clase anterior y que
# además tenga como atributos nombre y edad. Haz que sea posible
# instanciar un profesor dándole valor a todos los atributos.

class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

class Profesor(Staff):
    def __init__(self, role, dept, salary, nombre, edad):
        super().__init__(role, dept, salary)
        self.nombre = nombre
        self.edad = edad
    def __str__ (self):
        return (f"Role: {self.role}, Dept: {self.dept}, Salary: {self.salary}, Profesor: {self.nombre}, Edad: {self.edad}.")

profesor_1 = Profesor("Jefe de estudio", "Ingles", 2000, "Jose", 33)
print(profesor_1)
    
# 2º Representa el siguiente diagrama con sus clase, atributos y
# métodos correspondientes.
# Cada método display debe imprimir el nombre de la clases, 
# atributos y valores de la instancia en ese momento.
# Ejemplo: In displaymethodofParent1x=10.

class Parent1:
    def __init__(self, x):
        self.x = x
    def display(self):
        print(f"Indisplaymethodofparent1x = {self.x}")

class Parent2:
    def __init__(self, y):
        self.y = y
    def display(self):
        print(f"Indisplaymethodofparent2y = {self.y}")

class Child(Parent1, Parent2):
    def __init__(self, x, y, z):
        Parent1. __init__(self, x)
        Parent2. __init__(self, y)
        self.z = z
    def display(self):
        Parent1.display(self)
        Parent2.display(self)
        print(f"Indisplaymethodofchildz = {self.z}")

child_1 = Child(10, 30, 50)
child_1.display()

# 3º Crea una clase Car que herede de Vehicle y que sobreescriba 
# los métodos max_speed() y change_gear(). Instancia dos objetos
# de cada clase y comprueba que la salida de cada método es
# distinta.

class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def  show(self):
        print('Details:', self.name, self.color, self.price)
    def max_speed(self):
        print('Vehicle max speed is 150')
    def change_gear(self):
        print('Vehicle change 6 gear')

class Car(Vehicle):
    def __init__(self, name, color, price, model):
        super().__init__(name, color, price)
        self.model = model
    def  show(self):
        print('Details:', self.name, self.color, self.price, self.model)
    def max_speed(self):
        print(f'{self.model} car max speed is 150')
    def change_gear(self):
        print(f'{self.model} car change 6 gear')

vehicle = Vehicle("Turismo", "Negro", 1900)
car = Car("Toyota", "Negro", 1900, "4x4 L200")

vehicle.show()
vehicle.max_speed()
vehicle.change_gear()
car.show()
car.max_speed()
car.change_gear()

# 1º Dadas las siguientes clases con el output de sus respectivos 
# métodos, crea una interfaz formal que las implemente.

"""
svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data(data=none, y=None)
dt.fit()
dt.predict()

output:

Preprocessing data at SVM
Training at SVM
Evaluating at SVM
Preprocessing data at DecisionTree
Training at DecisionTree
Evaluating at DecisionTree
"""

from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def preprocess_data(self, data, y):
        pass
    @abstractmethod
    def fit(self):
        pass
    @abstractmethod
    def predict(self):
        pass

class SVM(Interface):
    def preprocess_data(self, data, y):
        print("Preprocessin data at SVM")
    def fit(self):
        print("Training at SVM")
    def predict(self):
        print("Evaluating at SVM")

class DecisionTree(Interface):
    def preprocess_data(self, data, y):
        print("preprocessing at DecisionTree")
    def fit(self):
        print("Training at DecisionTree")
    def predict(self):
        print("Evaluating at DecisionTree")

svm = SVM()
svm.preprocess_data(data = None, y = None)
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data(data = None, y = None)
dt.fit()
dt.predict()
    
# 2ª Repite el ejercicio anterior esta vez creando una interfaz informal. 

class Interface(ABC):
    def preprocess_data(self, data, y):
        pass
    def fit(self):
        pass
    def predict(self):
        pass

class SVM(Interface):
    def preprocess_data(self, data, y):
        print("Preprocessin data at SVM")
    def fit(self):
        print("Training at SVM")
    def predict(self):
        print("Evaluating at SVM")

class DecisionTree(Interface):
    def preprocess_data(self, data, y):
        print("preprocessing at DecisionTree")
    def fit(self):
        print("Training at DecisionTree")
    def predict(self):
        print("Evaluating at DecisionTree")

svm = SVM()
svm.preprocess_data(data = None, y = None)
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data(data = None, y = None)
dt.fit()
dt.predict()

# 3º Crea una clase virtual llamado Algoritmo con los atributos nombre;
# tarea y aprendizaje que sea superclase de la clase BaseClassifier del 
# problema anterior. Comprueba con el método issubclass que Algoritmo 
# es parte de BaseClassifier.

from abc import ABC, abstractmethod

class Algoritmo(ABC):
    def __init__(self, nombre, tarea, aprendizaje):
        self.nombre = nombre
        self.tarea = tarea
        self.aprendizaje = aprendizaje
    def prepocess_data(self, data, y):
        pass
    def fit(self):
        pass
    def predict(self):
        pass

class BaseClassifier(Algoritmo):
    def preprocess_data(self, data, y):
        print(f"preprocessing at {self.nombre}")
    def fit(self):
        print(f"training at {self.nombre}")
    def predict(self):
        print(f"Evaluating at {self.nombre}")

classifier = BaseClassifier(nombre = "SVM", tarea = "Clasificación", aprendizaje = "Supervisado")
classifier.preprocess_data(data = None, y = None)
classifier.fit()
classifier.predict()

print(issubclass(BaseClassifier, Algoritmo))

print("-------------------------------------------------")
# Mejor:

from abc import ABCMeta

class Algoritmo(metaclass = ABCMeta):
    def __init__(self, nombre, tarea, aprendizaje):
        self.nombre = nombre
        self.tarea = tarea
        self.aprendizaje = aprendizaje
    def prepocess_data(self, data, y):
        pass
    def fit(self):
        pass
    def predict(self):
        pass

Algoritmo.register(BaseClassifier)
print(issubclass(BaseClassifier, Algoritmo))

# 1º Escribe un script en Python para mostrar los distintos formatos de 
# fecha y hora. 

from datetime import datetime

ahora = datetime.now()

# a) Fecha y hora actuales
print(f"Fecha y hora:{ahora}")
# b) Año actual
print(f"Año:{ahora.year}")
# c) Mes del año
print(f"Mes: {ahora.strftime("%b")}")
# d) Número de la semana del año
print(f"Semana del año: {ahora.strftime("%u")}")
# e) Día de la semana
print(f"Día de la semana: {ahora.strftime("%a")}")
# f) Día del año
print(f"Día del año: {ahora.strftime("%j")}")
# g) Día del mes
print(f"Día del mes: {ahora.strftime("%d")}")
# h) Día de la semana
print(f"Día de la semana: {ahora.isoweekday()}")

# 2º Escribe un programa en Python para convertir una cadena a datetime. 

"""
INPUT : Jan 1 2014 2:43PM
OUTPUT : 2014-07-01 14:43:00
""" 

from datetime import datetime

cadena = "Jan 1 2014 2:43PM"
fecha = datetime.strptime(cadena, "%b %d %Y %I:%M%p")
print(f"Fecha: {fecha}")

# 3º Escribe un programa en Python para obtener la hora actual. 

from datetime import datetime

hora = datetime.now()
formato_hora = hora.strftime("%H:%M:%S")

print(f"Hora actual, {formato_hora}")

print("--------------------------------------------")

# Mejor:

import datetime
print(datetime.datetime.now().time())

# 4º Escribe un programa en Python para restar cinco días a la fecha 
# actual. 

from datetime import datetime, timedelta

fecha = datetime.now()
fecha_corregida = fecha - timedelta(days = 5)
formato_fecha = fecha_corregida.strftime(f"%b %d %Y")

print(f"Fecha actual, {formato_fecha}")

# 5º Escribe un programa en Python para convertir una cadena de marcas
# de tienpo unix en una fecha legible. 

"""
INPUT Unix timestamp string : 1284105682
OUTPUT : 2010-09-10 13:31:22
"""

from datetime import datetime, timezone

timestramp_string = "1284105682"
timetramp = int(timestramp_string)
fecha = datetime.fromtimestamp(timetramp, tz = timezone.utc)

print(fecha.strftime("%Y %m %d %H:%M:%S"))

print("---------------------------------------------")

# Mejor:

import datetime
print(datetime.datetime.fromtimestamp(int("1284105682")).strftime("%Y %m %d %H:%M:%S"))

# 6º Escribe un programa en Python para sumar 5 segundos con la hora actual. 

from datetime import datetime, timedelta

fecha = datetime.now()
fecha_corregida = fecha + timedelta(seconds = 5)
formato_fecha = fecha_corregida.strftime(f"%H:%M:%S")

print(f"Fecha actual, {formato_fecha}")

# 7º Escribe un programa en Python para obtener el número de la semana. 

from datetime import datetime

fecha = datetime.now()
semana = fecha.isocalendar()[1]

print(f"Semana: {semana}")

print("----------------------------------------------")

# Mejor:

import datetime
print(datetime.date(2015, 6, 16).isocalendar()[1])

# 8º Escribe un programa en Python  para seleccionar todos los domingos de
# un año determinado. 

from datetime import date, datetime

def los_domingos(anio):
    domingos = []
    for mes in range(1, 13):
        for dia in range(1, 32):
            try:
                fecha = date(anio, mes, dia)
                if fecha.weekday() == 6:
                    domingos.append(fecha)
            except ValueError:
                continue
    return domingos

anio = int(input("Introduce un año: "))
domingos_anio = los_domingos(anio)

for domingo in domingos_anio:
    print(domingo)

# 9º Escribe un programa en Python para contar el número de lunes del primer 
# día del mes desde 2015 hasta 2016. 

from datetime import date, datetime

def primer_lunes(anio_inicio, anio_final):
    lunes = 0
    for anio in range(anio_inicio, anio_final + 1):
        for mes in range(1, 13):
            primer_dia = datetime(anio, mes, 1)
            if primer_dia.weekday() == 0:
                lunes += 1
    return lunes

primeros_lunes_totales = primer_lunes(2015,2016)

print(f"Primeros lunes: {primeros_lunes_totales}")

# 10º Escribe un programa de Python para crear 12 fechas fijas a partir de una
# fecha especificada en un periodo determinado. La diferencia entre dos fechas 
# será de 20. 

from datetime import datetime, timedelta

def generar_fechas(inicio, cantidad, diferencia):
    fechas = []
    fecha_inicial = datetime.strptime(inicio, "%Y %m %f")
    
    for i in range(cantidad):
        nueva_fecha = fecha_inicial + timedelta(days = i * diferencia)
        fechas.append(nueva_fecha.strftime("%Y %m %d"))
    return fechas

fecha_inicio = input("Ingresa una fecha (año, mes, día): ")
fechas_elegidas = generar_fechas(fecha_inicio, 12, 20)

for fecha in fechas_elegidas:
    print(fecha)
    
# 1º Implementa una función generadora que dadas dos listas del mismo tamaño, 
# devuelva la multiplicación entre los elementos de cada una, el primer elemento
# de la lista 1 por el primero de la lista 2, el segundo con el segundo y así 
# sucesivamente. Sigue la siguiente estructura: 

"""
def prod(l1, l2):
    ...
    except StopIteration:
        pass
    return solution
"""

# Añadiendo el bloque except capturamos la excepción de Stop Iteration que se 
# produce al acabar de leer todos los elementos de un generador. 

def prod(l1, l2):
    if len(l1) != len(l2):
        raise ValueError("Listas de distinto tamaño.")
    def multiplicador():
        for a, b in zip(l1, l2):
            yield a * b

    mult = multiplicador()
    solucion = []
    try:
        while True:
            valor = next(mult)
            solucion.append(valor)
    except StopIteration:
        pass
    return solucion

lista1 = [1, 2, 3, 4, 5]
lista2 = [91, 92, 93, 94, 95]
resultado = prod(lista1, lista2)

print(f"Lista resultante: {resultado}")

# 2º Imprementa un generador, que dado un entero n, genere n números aleatorios.
# Puedes usar el método random de la librería random para generar números aleatorios. 

import random

def generador_aleatorio(n):
    for g in range(n):
        yield random.randint(0, 1000)

n = int(input("Longitud de secuencia aleatoria: "))
generador = generador_aleatorio(n)

for numero in generador:
    print(numero)

# 3º Implementa un generador de Fibonacci que genere n números de la secuencia de 
# Fibonacci, que itere la forma: 0, 1, 1,2 , 3, 5, 8, 13, ... Cuyos dos primeros valores
# son 0 y 1 por definición y el resto se calculan sumando los dos últimos valores de la
# sucesión. 

def fibonacci(n):
    a, b = 0, 1
    secuencia = []
    
    for f in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

n = int(input("Longitud de secuencia: "))
lista = fibonacci(n)

print(lista)

# 4º Implementa un generador, que dado un entero n, imprima todos los números inferiores
# a n multiplicados por dos. 

def multiplicador(n):
    resultado = []
    for numero in range(n):
        resultado.append((numero + 1) *2)
    return resultado

n = int(input("Multiplicamos por 2 hasta: "))

for numero in multiplicador(n):
    print(numero)

# 5º Implementa un generador, que dado un entero n, genere n números semanales. 

from datetime import datetime, timedelta

def generador_semanas(n):
    fechas = []
    fecha_hoy = datetime.now()
    for f in range(n):
        fechas.append(fecha_hoy)
        fecha_hoy += timedelta(weeks = 1)
    return fechas

n = int(input("Número de fechas: "))
generador = generador_semanas(n)

for f in generador:
    print(f.strftime(" %Y %m %d"))

# 1º Crea una función que genere una excepción e imprima su tipo, los argumentos de la 
# excepción y su mensaje de error. 

def excepcion():
    try:
        resultado = 1 / 0
    except Exception as error:
        print("Tipo: ", type(error))
        print("Argumento: ", error.args)
        print("Error: ", str(error))

excepcion()

# 2º Crea una función que compute la diferencia entre dos enteros. En caso de que la 
# diferencia sea negativa genera una excepción inventada por ti que informe sobre ello.
# Por ejemplo: la excepción podría llamarse NegativeDifferenceException. 

class NegativeDifferenceException(Exception):
    def __init__(self, error):
        self.error = error

def diferencia(a, b):
    resultado = a - b
    if resultado < 0:
        raise NegativeDifferenceException("Error, resultado negativo.")
    else: 
        print(resultado)
    return resultado

num1 = 6
num2 = 7

try:
    resultado = diferencia(num1, num2)
    print(f"Diferencia: {resultado}")
except NegativeDifferenceException as e: 
    print(e.error)

# 3º Crea una función que calcule la división entre dos números. Debe imprimir el mensaje 
# 'Los parámetros deben ser números enteros' cuando se genera una excepción de tipo y 
# 'El divisor no puede ser 0' cuando se genera un zerodivionerror.

def division(a, b):
    try:
        resultado = a / b
    except TypeError:
        print("Los parámetros deben ser números enteros")
        return None
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
        return None
    else: 
        print(f"Resultado: {resultado}")
    
division(1, 2)
division(1, "d")
division(1, 0)

# 4º Añade a la función anterior, un mensaje que se imprima al final de la ejecución de la
# función independientemente de si se ha generado excepción o no. 

def division(a, b):
    try:
        resultado = a / b
    except TypeError:
        print("Los parámetros deben ser números enteros")
        return None
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
        return None
    else: 
        print(f"Resultado: {resultado}")
    finally:
        print("FIN")

division(1, 2)
division(1, "d")
division(1, 0)
