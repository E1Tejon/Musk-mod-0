# FUNCIONES:

# Un funcion es un bloque reutilizable de código o declaraciones de programación diseñadas 
# para realizar una determinada tarea. 

# Para definir o delarar una función, Python proporciona la palabra "def". 

# Sintaxis para definir una función; El bloque de funciones de código se ejecuta colo si 
# se llama o invoca la función. 

# Declarar y llamar a una función:
# Cuando creamos una función, la llamamos declarar una función. 
# Cuando comenzamos a usarlo, lo llamamos ivocar o llamar una función. 
# La función se puede declarar con o sin parámetros. 

# Sintaxis:
 
def nombre_funcion(parametros):
    pass # Codigo o cuerpo de la función. "pass" se usa para continuar sin error.

# Ejercicio: Función sin parametros. 

def saludar():
    print("Bienvenido")

saludar()

# Ejercicio: Función con un parametro. 

def saludo(nombre):
    print(f"Hola {nombre}")

saludo("Che")
name = input("Dime un nombre: ")
saludo(name)

# Uso del "return" y diferencia con el "print". 

def despedir(nombre):
    frase = (f"Adios {nombre}")
    return frase

salida = despedir("Cheyenne")
print(salida)

print(despedir(name))

# Función con mas de un parametro:

def preimer_valor_mayor(num1,num2):
    if num1 > num2:
        return True
    else: 
        return False
    
def preimer_valor_mayor(num1,num2):
    return num1 > num2 # Ya hace lo de arriba. 

print(preimer_valor_mayor(20,3))

def sumar(num1,num2):
    return num1 + num2

print(sumar(5,9))

def sumar(num1,num2):
    return num1 + num2

resul = sumar(5,5)

print(sumar(resul,9)) # Así se puede llamar a una función dentro de una función.
print(sumar(sumar(5,5),9)) # O así tambien.

print("------------------------")

# Funciónes de argumentros con clave y valor. 

def restar(num1,num2):
    return num1 - num2

print(restar(num2 = 8, num1 = 9))

def restar(num1,num2,num3):
    return num1 - num2 - num3

print(restar(3, num3 = 8, num2 = 9)) #si no se nombra tiene que ir por prioridad de posición. 

# Funciones con parámetros predeterminados o por defecto. 

def multiplicar(num1 = 8, num2 = 9): # El num = x se ejecuta si no recibe un segundo valor.
    return num1 * num2

print(multiplicar(4,5)) # Cambia el valor de las variables.
print(multiplicar(9)) # Cambia la primera. 
print(multiplicar)

# Funciones con un número arbitratio de parametros. 

# Si no sabemos la cantidad de argumentos que pasamos a nuestra función,
# podemos crear una función que pueda tomar una cantidad arbitraria de argumentos
# agregando "*" antes del nombre del parámetro. 

def sumar(*nums): # Lo clasifica como tipo tupla para trabajar con ellos y sumarlos.
    return sum(nums) # "sum()" se usa para sumar todos los valores que le den. 

print(sumar(1, 2, 3))
print(sumar(1, 2, 3, 4))

# Si queremos pasar argujmentos en clave valor o directamente un diccionario podemos usar "**kwargs". 

def imprimir_detalles_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_detalles_persona(nombre = "Samuel", edad = 29, ciudad = "SantaCruz", ocupacion ="Mantenimiento")

numeros = [1, 2, 3, 4]

def listar(lista):
    for nombre in lista:
        print(nombre)

listar(numeros)

# Anotaciones en funciones. 

def sumar(num1:int, num2:int)-> int: # facilita, no restringe y devuelve con la condicón.
    return num1 + num2


def listar(lista: list, palabra: str): # Facilita la busqueda de funciones. 
    lista.append(palabra)

# EJERCICIOS:

# 1º Escribe una función llamada "contar_vocales" que tome una cadena como argumento y
# devuelva el número de voales en la cadena (sin importar mayúsculas o minusculas). 

def contar_vocales(frase: str):
    vocales = 0
    for letra in frase:
        if letra in "aeiou":
            vocales += 1
    return vocales

oracion = input("Escribe algo: ")
print(contar_vocales(oracion))

# 2º Declara una función llamada "add_item". El objetivo es agregar un elemento a una lista. 

lista = [1, 2, 3, 4, 5]

def add_item(listado:list,num:int):
    listado.append(num)
    return listado

print(add_item(lista,6))

# 3º Declara una función llamada "remove_item". El objetivo es borrar un elemento a una lista. 

def remove_item(lista: list,elemento):
    lista.remove(elemento)
    return lista

listado = ["a", 33, "otro"]
print(remove_item(listado,33))

# 4º Declara una función llamada "pares_e_impares". Deba retornar cuantos pares hay en una lista. 

def pares_e_impares(lista:list):
    cont = 0
    for par in lista:
        if par % 2 == 0:
            cont += 1
    return cont

print(pares_e_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 5º La temperatura en ºC se puede convertir a ºF usando esta fórmula: ºF = (ºC x 9/5) + 32. 
# Escribe una función que convierta ºC a ºF, "convert_clecius_to_fahrnheit". 



# 6º Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar 
# el área de un polígono. 
# - La función recibirá por parámetro sólo UN polígono a la vez. 
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectangulo. 
# - Imprime el cálculo del área de un polígono de cada tipo.
