# Haz un progama que devuelva el máximo de una secuencia de temperaturas acabada en 1000. 

num = int(input("introduce un número: "))
maximo = 0

while num != 1000:
    if num > maximo:
        maximo = num
    num = int(input("introduce un número: "))
print(f"El maximo de la secuencia es: {maximo}")