# Se usaran comparadores: 
# > menor que 
# < mayor que 
# >= mayor o igual que
# <= menor o igual que 
# == igualdad
# != desigualdad

# Los condicionales usaremos la palabra reservada "if" seguido de "else". 
# Ejemplo:

num1 = int(input("Introduzca un numero: "))

if num1 < 10:
    print("Es menor a 10")
else:
    print("Es mayor a 10")
    
print("Fin del programa")

# Para 3 condiciones o más usamos "elif".
# Ejemplo:

num2 = int(input("Introduzca un numero: "))

if num2 < 10:
    print("Es menor a 10")
elif num2 > 10:
    print("Es mayor a 10")
else:
    print("Es igual a 10")
    
print("Fin del programa")

# Operadores logicos: "and" (y) y el "or" (o):
# Ejemplo con "and":

num3 = int(input("Introduzca un numero: "))

if num3 % 3 == 0 and num3 % 5 ==0:
    print("Es multiplo de 3 y 5")
elif num3 % 3 == 0:
    print("Es multiplo de 3")
elif num3 % 5 ==0:
    print("Es multiplo de 5")
else:
    print("NO es multiplo ni de 3 ni de 5")
    
# Ejemplo con "or":

color = (input("Indique un color:"))

if color == "negro" or color == "morado" or color == "azul":
    print("color oscuro") 
elif color == "amarillo" or color == "naranja" or color == "rojo":
    print("color claro")
else:
    print("color neutro")
    
# Ejemplo de "if" anidado: 

num4 = int(input("Introduzca un numero: "))

if num4 < 10:
    print("Es menor a 10")
    if num4 % 2 == 0:
        print("par")
    else: 
        print("impar")
elif num4 == 10:
    print("igual a 10")
    print("primo")
else:
    print("Es mayor a 10")
    if num4 % 2 == 0:
        print("par")
    else:
        print("impar")
        
print("Fin del programa")

# Esribir un programa que almacene la cadena de caracteres contraseña en una variable,pregunte
# al usuario por la contraseña e imprima por la pantalla si la contraseña intrroducida por el 
# usuario coincide con la guardada en la variable. 

Contrasenya = "python" # No es recomendable usar "Ñ".
intento = input("¿Contraseña?") # (password) recomendable en ingles. :(

if Contrasenya == intento:
    print("acceso confirmado.")
else:
    print("acceso denegado.")
    
# Escribe un programa que solicite al usuario ingresar su edad y si tiene un carnet de estudiante
# (reponde "s" para sí y "n" para no). Verifica si la persona es menor de 25 años y tiene un carnet
# de estudiante. Si ambas condiciones se cumplen, imprime " Eres elegible para el descuento de estudiante"
# de lo contrario, imprime "no eres elegible para el descuento de estudiante". 

edad = int(input("ingrese su edad: "))
carnet = input("tiene carnet de estudiante: ")

if carnet != "n" and carnet != "s": #(DUDA, en la clase se puso "or" pero en caso de una True la otra False y "or" siempre es True)
    print("Entrada no valida")
elif edad <= 25 and carnet == "s":
    print("Eres elegible para el descuento de estudiante")
else:
    print("no eres elegible para el descuento de estudiante")
    if edad >= 25:
        print("supera el limite de edad")
    if carnet == "n":
        print("no posee un carnet de estudiante") 

# Clasificación de edad: solicita al usuario que ingrese su edad y clasifícala en "niño" (0-12 años),
# "adolescente" (13-17 años), "adulto joven" (18-25 años), "adulto" (26-64 años), o "adulto mayor" (>=65 años). 

Edad = int(input("Edad: "))

if Edad <= 0: # Pendiente aprender a pasar los valores de pantalla a absoluto.
    print("prenato")
elif Edad <= 12:
    print("niño")
elif Edad <= 17:
    print("adolescente")
elif Edad <= 25:
    print("adulto jovel")
elif Edad <= 64:
    print("adulto")
else:
    print("adulto mayor")