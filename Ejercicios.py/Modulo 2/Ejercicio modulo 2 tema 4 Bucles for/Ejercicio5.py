# 5º Haz un programa que lea un número y lo escriba del revés. 

numero = int(input("Escribe un número: "))
n = ""

while numero > 0:
    n += str(numero % 10) # Esto lo tube que mirar, no lo acabe de entender.
    numero = numero // 10
print(n)