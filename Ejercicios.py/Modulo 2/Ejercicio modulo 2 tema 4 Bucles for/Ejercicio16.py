# 16º Haz un programa que dada una secuencia de valores enteros acabada en 0, 
# diga cuántos son múltiplos del primero. 

num = int(input("Introduce un número: "))
primer_num = 0
conteo = 0
conteo_multiplos = 0

while num != 0: 
    if conteo == 0:
        primer_num = num
        conteo += 1
    elif num % primer_num == 0:
        conteo_multiplos += 1
    num = int(input("Introduce un número: "))

print(f"En esta secuencia hay {conteo_multiplos} múltiplos de {primer_num}")