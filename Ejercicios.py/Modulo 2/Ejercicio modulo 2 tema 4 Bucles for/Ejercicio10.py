# 10º Haz un programa que cuente cúantos valores hay en una secuencia de enteros acabada en 0. 

num = int(input("Introduce un número: "))
conteo = 0

while num != 0:
    conteo += 1
    num = int(input("Introduce un número: "))
print(f"La secuencia tiene {conteo} elementos.")