# 1º Haz un programa que lea dos números a y b, y que escriba todos los números enteros a y b. 
# Debe cumplirse que a < b. En caso que a > b, escribe los números de manera descendente. 

a = int(input("Introduzca un valor: "))
b = int(input("Introduzca un valor: "))

if a < b:
    for e in range(a, b+1, 1):
        print(e)
else: 
    for e in range(a, b-1, -1):
        print(e)