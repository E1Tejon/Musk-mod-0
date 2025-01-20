# 14º Haz un programa que dada una secuencia de valor acabada en 0, diga si hay más positivos o negativos. 

n = int(input("introduce un número: "))
positivos = 0
negativos = 0

while n != 0:
    if n > 0:
        positivos += 1
    else:
        negativos += 1
    n = int(input("introduce un número: "))
    
if positivos > negativos:
    print(f"Hay {positivos - negativos} positivos mas que negativos.")
elif positivos == negativos:
    print("hay tantos positivos como negativos.")
else:
    print(f"Hay {negativos - positivos} negativos mas que positivos")