# 9º Haz un programa que reciba una secuencia denaturales de tamaño "n" y nos 
# devuelva cuál es el primer natural que tiene un valor inferior al primer natural leído

n = int(input("Introduce el tamaño de la secuencia: "))

for x in range(0, n):
    digito =int(input("Digito: "))
    if x == 0: 
        natural1 = digito
    elif digito < natural1:
        print(f"El 1º natural inferior a {natural1} es {digito}")
        break
    