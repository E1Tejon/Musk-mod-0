# BUCLE WHILE. 
# Se usa con la palabra reservada "while", para ejecutar un bucle de 
# declaraciones repetidamente hasta que se cumple una condición determinada. 
# Cuando la condición se vuelve falsa, las lineas de código después del bucle continuarán ejecutándose. 
# Se puede sistituir la condición por un dato booleano o por una vriable que contenga un tipo booleano. 

# Sintasis:
# while condicón:
#    código

# Ejemplo: Prints from 0 to 4

numero = 0 # variable externa a la que ponerle la condición. 
while numero <= 5: # 0 < 5 ? true, 1 < 5 ? true,... 6 < 5 ? false. 
    print(numero) # 0, 1, ..., 5. 
    numero += 1 # numero = numero + 1

# Si ejecutamos un bloque de código una vez que la condición ya no sea cierta, podemos unsar "else". 

# Ejemplo: 

numero = 0

while numero <= 5: 
    print(numero)
    numero += 1
else: 
    print("proceso completado.")

# Break: usamos "break" cuando queremos salir o detener el ciclo.

# Ejemplo: (Atención al orden).

numero = 0

while numero <= 5: 
    if numero == 3: # Printa del 0 al 2 y para.
        break
    print(numero)
    numero += 1
else: 
    print("proceso completado.")

# Ejemplo:

numero = 0

while numero <= 5: 
    print(numero)
    if numero == 3: # Printa del 0 al 3 y para.
        break
    numero += 1
else: 
    print("proceso completado.")

# Continuar: instrucción para omitir la iteración y continuar con la siguiente. 

# Ejemplo: 

numero = 0

while numero <= 5:
    if numero == 3: # Saltara el 3 y continuará con la secuencia. 
        numero += 1 # Hay que incrementar dentro del continue o se quedara en la condición.
        continue
    print(numero)
    numero += 1
else: 
    print("proceso completado.")

# Para que el bucle pare con un break :

# Ejemplo: (sin marca o señal)

numero = 0

while True: # Bucle infinito que solo acaba con un "break". 
    if numero == 6:
        break
    print(numero)
    numero += 1
else: 
    print("proceso completado.")

# Ejemplo: (con marca o señal)

numero = 0
senyal = True # Marca o señal. 

while senyal: 
    if numero == 6:
        senyal = False
    print(numero)
    numero += 1
else: 
    print("proceso completado.")

# Ejercicios:

# 1º Imprime los numeros del 1 al 100. 

numero = 0

while numero <= 100:
    print(numero)
    numero += 1

