# 13º Haz un programa que dada una secuencia de valor acabada en 0, compruebe que ningún valor supere 50
# y que no haya más de 3 que superen el 40.

n = int(input("introduce un número: "))
mayor50 = False
mayor40 = False
conteo40 = 0

while n != 0:
    if n > 50:
        mayor50 = True
    if n > 40:
        conteo40 += 1
    if conteo40 > 3:
        mayor40 = True
    n = int(input("introduce un número: "))

if mayor50 == True: # En el ejercicio resuelto se ahorran el " == True" ¿eso es una forma de abreviar?
    print("Hay valores superiores a 50 en la secuencia.")
else: 
    print("No hay valores superiores a 50 en la secuencia")
if mayor40 == True:
    print("Hay mas de 3 valores superiores a 40 en la secuencia.")
else: 
    print("No hay mas de 3 valores superiores a 40 en la secuencia")