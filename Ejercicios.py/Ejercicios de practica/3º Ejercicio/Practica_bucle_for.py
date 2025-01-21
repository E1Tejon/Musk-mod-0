# Bucle o loop: acción que se repite.
# For se utiliza para iterar (repetir) una secuencia de ojetos iterables:
# (listas, tuplas, diccionarios, conjuntos o cadenas.)
# "for": se usa sin condición, se conoce el número de iteracione. 
# "while": se usa con condiciones, determinan las iteraciones.

# Sintasis:

#for x in ojeto_iterable:     # x es una variable interna para el bucle, su valor varia con cada iteración.
#    pass                     # que hacemos dentro del bucle. 

# Bucle sobre un string:

lenguaje = "python" # Los enteros y boolianos no es un dato al que se pueda hacer un bucle.

for letra in lenguaje:
    print(letra)

# Bucles sobre una lista:

lista_colores = ["rojo", "verde", "negro"]
lista_cosas = ["peras", 4, True , 3.5, lista_colores]

for color in lista_colores:
    print(color)

for cosas in lista_cosas:
    print(cosas)

# La función rango (range):
# Se utiliza como una lista de números. [1, 2, 3, 4, 5, 6]
# El rango toma tres parametros:
# Inicio, Fin e Incremento (inici, fin, paso). De forma predeterminada, comienza desde 0 y el incremento es 1.
# Hay que tener en cuenta que el fin nunca se incluye, es decir si se hace range(1,10) este rango acaba en 9.
# La secuencia de rango necesita al menos un argumento (fin). 

# Ejemplo: ver que printa el rango de 11. 

for num in range(11): # La lista empezará por 0.
    print(num)

# Ejemplo: ver que printa el rango de 1 a 11. 

for num in range(1,11): # La lista empezará por 1.
    print(num)

numero = 22

for num in range(numero): # Se puede hacer un rango de una variable.
    print(num)

# Ejemplo: ver que printa el rango de 1 a 11 con salto 2. 

for num in range(1,11,2):
    print(num)

# Ejemplo: ver que printa un rango de 10 a 0 hacia atras. 

for num in range(10,-1,-1):
    print(num)

# Usar el else con bucle for:

for num in range(1,6):
    print(num)
else:
    print("Se acabo el bucle") # Así con un else se puede comprobar que no hay "break", (se rompa el bucle). 
    
# Break en un bucle:

for num in range(1,6):
    if num == 3:
        break # Se rompe el bucle y  no aparece el else.
    print(num)
else:
    print("Se acabo el bucle")

# NO es recomendable crear variables dentro de un bucle, se deben crear fuera del bucle: 
# Ejemplo: 

color = "rojo"
vocal_o = 0

for letra in color:
    if letra == "o":
        vocal_o += 1
print(vocal_o)

print("----------------")

# Ejercicio:
# 1. Escribe un programa que imprima todos los números del 1 al 10. 

for num in range(1,11):
    print(num)

# 2. Escribe un programa que imprima los números pares del 1 al 20. 

for num in range(1,21):
    if num % 2 == 0:
        print(num)

# 3. Escribe un programa que calcule la suma de los primeros 10 números naturales.

suma = 0 
for num in range(1,11):
    suma += num
print(suma)

# 4. Escribe un programa que imprima la tabla de multiplicar del 5.

tabla = 5

for num in range(1, 11):
    print(f"{tabla} X {num} = {num*tabla}")

# 5. Escribe un programa que imprima los números del 1 al 100,
# pero que reemplace los múltiplos de 3 por "Fizz", loos múltipos de 5 por "Buzz" y 
# los múltipos de ambos por "FizzBuzz". 

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else: 
        print(num)

# Ahora guarda los resultados en una lista y pinta la lista. 

lista = []

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        lista.append("fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
        lista.append("fizz")
    elif num % 5 == 0:
        print("Buzz")
        lista.append("buzz")
    else: 
        print(num)
        lista.append(num)
print(lista)

# Ahora guarda los resultados en un diccionario. 

diccionario = {}

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        diccionario[num] = "fizzbuzz"
    elif num % 3 == 0:
        print("Fizz")
        diccionario[num] = "fizz"
    elif num % 5 == 0:
        print("Buzz")
        diccionario[num] = "buzz"
    else: 
        print(num)
        diccionario[num] = num
print(diccionario)

# 6. Escribe un programa que imprima la secuencia de Fibonacci hasta el décimo número.

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
n = 10
fibonacci = fibonacci_sequence(n)
print("Secuencia de Fibonacci hasta el décimo número:")
print(fibonacci)

# 7. Escribe un programa que encuentre e imprima los números primos menores de 100.

print("Números primos menores de 100:")
for num in range(2, 100):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)
        