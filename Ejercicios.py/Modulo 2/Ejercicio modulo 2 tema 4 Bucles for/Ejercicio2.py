# 2º Haz un programa que lea la secuencia de 10 números y que escriba la media.

suma = 0
for n in range(0,10):
    num = int(input("Introduce un número: "))
    suma += num
print(f"Media: {suma/10}")