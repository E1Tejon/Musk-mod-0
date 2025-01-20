# Ejercicios:

# 1º Imprime los numeros del 1 al 100. 

numero = 0

while numero <= 10:
    print(numero)
    numero += 1

# 2ª Tabla de multiplicar específica: Pide un número y luego imprime la tabla de
# multiplicar de ese número del 1 al 10. 

num = int(input("Escriba un número: "))
mult = 0

while mult <= 10:
    print(f"{num}  x {mult}  = {num * mult}" )
    mult += 1

# 3º Pide al usuario que escriba una palabra, y cuenta cuantas letras tiene esa palabra. 

palabra = input("Escriba una palabra: ")
n = 0

while n < len(palabra): # "len": mientras "n" sea menor que la palabra le sumas 1 a "n".
    n += 1
print(f"{palabra} contiene {n} letras.")

# 4º Escribe un programa que pregunte una y otra vez si desea continuar con el programa, 
# siempre que conteste "si" me tiene que volver a preguntar. 

pregunta = input("¿Quieres seguir ejecutando el programa?: ")

while pregunta == "si":
    pregunta = input("¿Quieres seguir ejecutando el programa?: ")
    if pregunta == "no":
        print("O.K.")

# 5º Imprime el siguiente patron de estrellas:
# *
# **
# ***
# ****
# *****

numero_filas = 1

while numero_filas <= 5:
    print(numero_filas * "*")
    numero_filas += 1

# 6ª Escribe un programa que genere un número al azar del 1 al 10, pide al usuario que 
# adivine el numero, si adivina muestra un mensaje de felicitación, si no lo adivina pidele 
# que ingrese otro número. 

import random                              #
#                                          # genera un número aleatorio. 
numero_secreto = random.randint(1,10)      #
intento = int(input("Adivina el número: "))

while True:
    if  intento == numero_secreto:
        print("Felicidades")
        break
    elif intento <= numero_secreto:
        print("Más alto ")
    elif  intento >= numero_secreto:
        print("Más bajo ")
    intento = int(input("Prueva con otro: "))