# 15º Haz un programa que dada una secuencia de valores enteros acabada en 0,
# que diga cuál es el número que hay antes del primer negativo. 

num = int(input("Introduce un número: "))
num_pre = 0

while num_pre != 0:
    if num > 0:
        num_pre = num
        num = siguiente
        siguiente = int(input("Introduce un número: "))
    
if num < 0:
    print(f"El número anterior al primer negativo es: {num_pre}")
else: 
    print("No hay negativos en esta secuencia.")