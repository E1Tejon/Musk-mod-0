# 4º Haz un programa que lea un número n y que escriba la "tabla de multiplicar de n". 

num =int(input("Introduce un número: "))

for x in range(0,11):
    print(f"{num} x {x} = {num * x}")
    