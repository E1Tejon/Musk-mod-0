# 1. Haz un programa que lea una secuencia de caracteres acabada en punto
# y que escriba cuántas letras ‘a’ contiene.

secuencia = input("Escribe una frase: ")
a = 0
for letra in secuencia:
    if letra == "a":
        a += 1
print(f"La letra a se repite {a} veces.")

# 2. Haz un programa que encuentre todas las apariciones de una subcadena en una cadena dada.

cadena = input("Escribe una frase: ")
subcadena = input("Escribe una subcadena: ")
conteo = cadena.count(subcadena.lower())

print(f"En la frase {cadena} se repite {subcadena}, {conteo} veces")

# 3. Haz un programa que invierta una cadena dada.

cadena = input("Escribe una frase: ")

print(cadena[::-1])

# 4. Haz un programa que divida una cadena en guiones.

cadena = input("ingresa una cadena: ")
cadena_guiones = ""
espacio = " "

for letra in cadena:
    if letra not in espacio:
        cadena_guiones += letra
    else: 
        cadena_guiones += "-"

print(cadena_guiones)


# 5. Haz un programa que añada una nueva cadena en medio de una cadena dada.

cadena1 = input("ingresa una cadena: ")
cadena2 = input("ingresa una subcadena: ")
mitad = int(len(cadena)// 2)
solucion = cadena1[:mitad] + cadena2 + cadena1[mitad:]

print(solucion)

# 6. Haz un programa que encuentre la última posición de una subcadena dada.

cadena1 = input("ingresa una cadena: ")
cadena2 = input("ingresa una subcadena: ")
ultima_posicion = -1

for letra in range(len(cadena1) - len(cadena2) + 1):
    if cadena1[letra:letra + len(cadena2)] == cadena2:
        ultima_posicion = letra

if ultima_posicion != -1:
    print(f"La última posicion de {cadena2} es: {ultima_posicion} ")
else: 
    print(f"{cadena2} no se encuentra en {cadena1}")

# 7. Haz un programa que elimine cadenas vacías de una lista de cadenas.

cadena = input("Escribe una cadena: ")
cadena_sin_espacio = ""

for letra in cadena:
    if letra != " ":
        cadena_sin_espacio += letra

print(cadena_sin_espacio)

# 8. Haz un programa que elimine símbolos especiales / signos de puntuación de una cadena.

cadena = input("ingresa una cadena: ")
cadena_sin_simbolos = ""
simbolos = "¡!\#$%&'()*+,-./:;<=>¿?@[]^_`{|}~"

for letra in cadena:
    if letra not in simbolos:
        cadena_sin_simbolos += letra

print(cadena_sin_simbolos)

# 9. Haz un programa que encuentre palabras con letras y números.

cadena_palabras = input("ingresa una cadena: ")
palabras_numero = ""

for letra in cadena_palabras:
    if letra == " ":
        posicion = len(letra)
        palabra = cadena_palabras[:posicion] 
        for numero in palabra:
            if numero == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                palabras_numero += palabra

print(palabras_numero) # MAL

# 10. Haz un programa que sustituya cada símbolo especial por # en la siguiente cadena.

cadena = input("ingresa una cadena: ")
cadena_cambiada = ""
simbolos = "¡!\#$%&'()*+,-./:;<=>¿?@[]^_`{|}~"

for letra in cadena:
    if letra not in simbolos:
        cadena_cambiada += letra
    else: 
        cadena_cambiada += "#"

print(cadena_cambiada)

# LISTAS:

# 1. Haz un programa que lea una lista dado su tamaño e imprima el segundo elemento (si existe).

longitud = int(input("Ingresa la longitud de la lista: "))
lista = []

for variables in range(0 ,longitud):
    variable = input("ingresa una varible: ")
    lista.append(variable)
if len(lista) > 1:
    print(f"La segunda variable es: {lista[1]}")
else: 
    print("No hay segundas variables en la lista.")
    
# 2. Haz un programa que lea una secuencia no vacía de enteros acabada en -1,
# y que escriba cuántos son iguales al último.

variable = int(input("ingresa un número: "))
lista = []

while variable != -1:
    lista.append(variable)
    variable = int(input("ingresa un número: "))

if lista:
    ultimo = lista[-1]
    conteo = lista.count(ultimo) - 1
    print(f"Hay {conteo} variables iguales a {ultimo}.")
else: 
    print("No hay ninguna variable antes de -1.")

# 3. Haz un programa que lea secuencias de enteros acabada en -1, 
# y que escriba cada una invirtiendo el orden de sus elementos.

variable = int(input("ingresa un número: "))
lista = []

while variable != -1:
    lista.append(variable)
    variable = int(input("ingresa un número: "))
lista.reverse()
print(lista)

# 4. Haz un programa que lea n palabras, y que escriba cada una invirtiendo el orden de sus caracteres.

longitud = int(input("indica la logitud de la lista: "))
lista = []

for palabra in range(0, longitud):
    variable = input("escribe una palabra: ")
    variable_inversa = variable[::-1]
    lista.append(variable_inversa)

print(lista)

# 5. Haz un programa que lea una secuencia de números mientras sean positivos y que escriba la media.

variable = int(input("ingresa un número: "))
lista = []
suma = 0
while variable > 0:
    lista.append(variable)
    suma += variable
    variable = int(input("ingresa un número: "))
    
print(suma / len(lista))

# 6. Haz un programa que devuelva la concatenación de v1 y v2, v1 y v2 son dos listas de tamaño n y m. Es decir,
# hay que devolver un vector que tenga los elementos de v1 seguidos de los elementos de v2.

v1 = []
n = int(input("longitud de lista: "))

for variables in range(0, n):
    variable = (input("ingresa un número: "))
    v1.append(variable)

v2 = []
m = int(input("longitud de lista: "))

for variables in range(0, m):
    variable = (input("ingresa un número: "))
    v2.append(variable)

v3 = v1 + v2

print(v3)

# 7. Haz un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
# y muestre por pantalla el menor y el mayor de los precios.

lista = [50, 75, 46, 22, 80, 65, 8]

print(min(lista))
print(max(lista))

# 8. Haz un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for asignatura in asignaturas:
    print(asignatura)

# 9. Haz un programa que almacene en una lista los números del 1 al 10 y 
# los muestre por pantalla en orden inverso separados por comas.

lista = list(range(1, 11))
lista.reverse()
resultado = str(lista[0])

for variable in (lista[1:]):
    resultado += ", " + str(variable)

print(resultado)

# 10. Haz un programa que concatene dos listas del mismo tamaño n alternando elementos de una lista y otra.

n = int(input("longitud de lista: "))

lista1 = []

for variables in range(0, n):
    variable = (input("ingresa un número: "))
    lista1.append(variable)

lista2 = []

for variables in range(0, n):
    variable = (input("ingresa un número: "))
    lista2.append(variable)

lista3 =[]

for variables in range(0, n):
    lista3.append(lista1[variable]) # Aquí hay algo mal
    lista3.append(lista2[variable])

print(lista3)

# 11. Haz un programa que itere ambas listas de tamaños n y m (siendo n y m números distintos )
# simultáneamente e imprima sus elementos. MAL

n = int(input("longitud de lista: "))
m = int(input("longitud de lista: "))

lista1 = []

for variables in range(0, n):
    variable = (input("ingresa un número: "))
    lista1.append(variable)

lista2 = []

for variables in range(0, m):
    variable = (input("ingresa un número: "))
    lista2.append(variable)

longitud1 = 0
longitud2 = 0

while longitud1 < len(lista1) or longitud2 < len(lista2):
    if longitud1 < len(lista1):
        print(lista1[longitud1])
    if longitud2 < len(lista2):
        print(lista2[longitud2])
    longitud1 = 1
    longitud2 = 1

# 12. Haz un programa que añada un nuevo elemento 60 a la lista [10, 50, 40, 20, 30] 
# después de un elemento especificado por el usuario. Si el elemento introducido no
# está presente en la lista debe mostrar el mensaje: 'Elemento no presente en la lista'.

lista = [10, 50, 40, 20, 30]
variable = int(input("Ingresa una variable de la lista: "))
añadir = 60

if variable in lista:
    posicion = lista.index(variable)
    lista.insert(posicion + 1, añadir)   
    print(lista)
else:
    print("No esta en la lista.")

# 13. Haz un programa que elimine todas las apariciones de un elemento específico introducido
# por el usuario de la lista [10, 50, 40, 20, 60, 30].

lista = [10, 50, 40, 20, 60, 30]
variable = int(input("Ingresa una variable de la lista: "))

while variable in lista:
    lista.remove(variable)

print(lista)

# TUPLAS:

# 1. Haz una programa que invierta una tupla.

tupla = (10, 50, 40, 20, 60, 30)
invertida = tupla[::-1]

print(invertida)

# 2. Haz un programa que acceda al valor 15 de la tupla.

tupla = (10, 50, 40, 20, 60, 30, 70, 15,"rojo")

print(tupla[8])

# 3. Haz un programa que declare una tupla con un solo elemento 10.

tupla = (10)

print(tupla)

# 4. Haz un programa que descomponga la tupla en 4 variables.

tupla = (1, 2, 3, 4)
a, b, c, d = tupla

print(a)
print(b)
print(c)
print(d)

# 5. Haz un programa que intercambie dos tuplas en Python.

tupla1 = (0, 1)
tupla2 = (2, 3)
tupla1, tupla2 = tupla2, tupla1

print(tupla1)
print(tupla2)

# 6. Haz un programa que copie elementos específicos de una tupla a una nueva tupla.

tupla1 = (0, 1, 2, 3, 4)
tupla2 = tupla1[3:]

print(tupla2)

# 7. Haz un programa que modifique una tupla.

tupla = (1, 2, 3,[0, 5], 4, 5)
lista = list(tupla)
lista[3],[1] = 6
tupla = tuple(lista)

print(tupla)

# 8. Ordena una tupla de tuplas por el 2º elemento.

tupla = ((4, 3), (3, 2), (2, 1), (1, 0))
lista = list(tupla)
variable = tupla[0]
lista.remove((4, 3))
lista.insert(1, variable)
tupla = tuple(lista)

print(tupla)

# 9. Haz un programa que cuente el número de apariciones del elemento 50 de una tupla.

tupla = (1, 2, 3, 4, 3, 2, 1)

print(tupla.count(3))

# 10. Haz un programa que compruebe si todos los elementos de la tupla son iguales.

tupla = (10, 10, 10, 10)
conteo = 1

while conteo < len(tupla) and tupla[conteo - 1] == tupla[conteo]:
    conteo += 1
if conteo == len(tupla):
    print("Todas las variables de la tupla son iguales.")
else: 
    print("Todos los elementos de la tupla no son iguales.")
