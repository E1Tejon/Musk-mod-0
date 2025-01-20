# 3º Haz un programa que dada una lista de naturales de tamaño n, indique la posición del primer número par. 

n =int(input("Tamaño de la secuencia: "))

if n > 0:
    for e in range(0, n):
        num = int(input("Introduce un número: "))
        if num % 2 == 0:
            print(f"Primer Nº par: {num}, en la posición: {e}. ")
            break
else: 
    print("No hay primos en la secuencia.")