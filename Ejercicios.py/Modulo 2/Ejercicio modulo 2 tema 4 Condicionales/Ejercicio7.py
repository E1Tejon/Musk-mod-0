# 7º Haz un programa que lea un real x >= 0 y que escriba:
# [x] (parte entera inferior), [x] (parte entera superior), Redondero: (redondeo de x). 

x = float(input("Introduzca un número decimal: "))
x_int = int(x)
int_inferior = x_int
int_superior = x_int + 1
redondeo = int(x + 0.5)

if x == x_int:
    print(x)
else: 
    print(f"[x]: {int_inferior}, [x]: {int_superior}, Redondeo: {redondeo}")
    