# 18º Haz un programa que lea un natural n, y que escriba el resultado de
# la suma siguiente: 1^2 + 2^2 + … + (n−1)^2 + n^2 y el aspecto de la secuencia. 

n =int(input("Longitud de secuencia: "))
suma = 0
secuencia = 0

for i in range(0, n + 1):
    suma += (i**2)
    if i == 0:
        secuencia = f"{i}^{2}"
    else: 
        secuencia +=  f" + {i}^{2}"
    
print(f"La secuencia {n} y su suma se expresan: {secuencia} = {suma}")
        