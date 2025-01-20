# 6º Haz un programa que lea un número y que escriba el número de díjitos. 

numero = int(input("Introduce un número: "))
conteo = 0
x = numero # ¿si la variable "x" no se nombra en el "while" no cambia como la variable "numero"?

while numero > 0:
    numero = numero // 10 # Esto no me queda del todo claro
    conteo += 1
print(f"{x} tiene {conteo} dígitos.")
