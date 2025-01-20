# FUNCIONES

# 1. Haz un programa que cree una función en Python que dada una secuencia devuelva únicamente los números pares.

def busca_pares(secuencia):
    pares = []
    for elemento in secuencia:
        if elemento % 2 == 0:
            pares.append(elemento)
    return pares

lista = [1, 2, 3, 4, 5, 6, 7, 8]
pares = busca_pares(lista)

print(pares)

# 2. Haz un programa que cree una función con longitud variable de argumentos.

def funcion_variable(*argumentos):
    for elementos in argumentos:
        print(elementos)
        
funcion_variable(1, 2, 3, 4, 5)

# 3. Haz un programa que devuelva múltiples valores desde una función.
# Crea la función calculaion() de modo que pueda aceptar dos variables y calcular sumas y restas.
# Además, debe devolver tanto la suma como la resta en una sola llamada.

def calculaion(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    return suma, resta

print(calculaion(5,10))

# 4. Haz un programa que cree una función con un argumento por defecto.
# Crea una función show_employee() usando las siguientes condiciones.
# -Debe aceptar el nombre y el salario del empleado y mostrar ambos.
# -Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al salario.

def show_employee(nombre, salario = 9000):
    print(f"nombre: {nombre}, salario: {salario}")

show_employee("Juan")

# 5. Haz un programa que cree una función interna para calcular la suma de la siguiente manera:
# Crea una función externa que acepte dos parámetros, a y b. 
# Crea una función interna dentro de una función externa que calculará la suma de a y b.
# Por último, una función externa que sumará 5 en la suma y la devolverá.

def funcion_externa(num1, num2):
    def suma(num1, num2):
        return num1 + num2
    resultado1 = suma(num1, num2)
    return  resultado1 + 5

print(funcion_externa(2, 3))

# 6. Haz un programa que cree una función que escriba el cuadrado y la raíz cuadrada de una secuencia de naturales.

def cuadrado_raiz(num):
    for elemento in num :
        cuadrado = elemento ** 2
        raiz = elemento ** 0.5
        print(f"el cuadrado de {elemento} es: {cuadrado} y su raiz: {raiz}")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cuadrado_raiz(lista)

# 7. Haz un programa que cree una función que deje a, b y c ordenados de pequeño a grande.
# Por ejemplo, si a =7, b = −3 y c = 1, los valores después de la llamada deben ser a =−3, b = 1 y c = 7.

def ordenar_lista(listado):
    listado.sort()
    return listado

lista = [1, 9, 2, 8, 3, 7, 4, 6, 5]

print(ordenar_lista(lista))

print("------------------------------------------------")

# Los Ejercicios de repaso de la clase grabada: Funciones. 

# 8º La temperatura en ºC se puede convertir a ºF usando esta fórmula: ºF = (ºC x 9/5) + 32. 
# Escribe una función que convierta ºC a ºF, "convert_celcius_to_fahrenheit". 

def convert_celcius_to_fahrenheit(celcios:float):
    fahrenheit = (celcios * 9/5) + 32 # NO me permite multiplicar "floats" ¿por qué?
    return fahrenheit

temperatura = float(input("temperatura en ºC: "))

print(f"{convert_celcius_to_fahrenheit(temperatura)} ºK")

# 9º Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar 
# el área de un polígono. 
# - La función recibirá por parámetro sólo UN polígono a la vez. 
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectangulo. 
# - Imprime el cálculo del área de un polígono de cada tipo.

def area_poligonos(poligono):
    if poligono == "triangulo":
        altura = float(input("Altura del triángulo: "))
        base = float(input("Base del triángulo: "))

        if altura and base:
            return (base * altura) / 2
        else: 
            return "Faltan parametros para calcular el área del triángulo"
    elif poligono == "cuadrado":
        lado = float(input("Lado del cuadrado: "))
        if lado:
            return lado * lado
        else: 
            return "Faltan parametros para calcular el área del cuadrado"
    elif poligono == "rectangulo":
        base = float(print("Base del rectángulo: "))
        altura = float(print("Altura del rectángulo: "))
        if base  and altura:
            return (base * altura)
        else: 
            return "Faltan parametros para calcular el área del rectángulo"
    else: 
        return "No se reconoce el polígono"

eleccion_poligono = input("Ingresa un polígono: ")
print(area_poligonos(eleccion_poligono))