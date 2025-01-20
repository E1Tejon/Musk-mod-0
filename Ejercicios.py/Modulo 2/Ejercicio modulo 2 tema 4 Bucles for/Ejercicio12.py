# 11º Haz un programa que dada una secuencia de valores acabada en 0, comprueve que ningun valor supera 50.

num = int(input("introduce un número: "))
mayor50 = False

while num != 0:
    if num > 50:
        mayor50 = True
        break
    num = int(input("introduce un número: "))

if mayor50:
    print("Hay valores superiores a 50 en la secuencia.")
else: 
    print("No hay valores superiores a 50 en la secuencia")