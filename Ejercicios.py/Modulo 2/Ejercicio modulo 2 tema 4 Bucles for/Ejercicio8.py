# 8º Haz un programa que dada una secuencia de años acabados en 0, nos diga cuántos hay del siglo 20. 

anyo = int(input("Introduce un año: "))
conteo = 0

while anyo != 0:
    siglo = anyo // 100 # Aqui si veo claro como se usa "//"
    if siglo + 1 == 20:
        conteo += 1
    anyo = int(input("Introduce un año: "))
    
print(f"{conteo} años son del siglo 20")
