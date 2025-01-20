# 4º Haz un programa que, dados dos intervalos, calcule el intervalo
# correspondiente a la intersección o indique que es esta es vacía. 

num1 = int(input("mínimo del primer intervalo: "))
num2 = int(input("maximo del primer intervalo: "))
num3 = int(input("mínimo del segundo intervalo: "))
num4 = int(input("maximo del segundo intervalo: "))

Mínimo = num1
Maximo = num2

if num3 > num1:
    Mínimo = num3
if num4 > num2:
    Maximo = num4

if Mínimo <= Maximo:
    print(f"[{Mínimo},{Maximo}]")
else: 
    print("[-,-]")