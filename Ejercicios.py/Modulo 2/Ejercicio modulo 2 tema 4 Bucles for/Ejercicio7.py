# 7º Haz un programa que lea un número y diga si es capicua o no. 

numero = int(input ("Introduce un número: "))
x = str(numero)
i = 0
j = len(x) - 1

while i < len(x)-1 and j > 0 and x[i] == x[j]: # Lo acabe por copiar, no lo acabo de entender.
    i += 1
    j -= 1
    
if j == 0 and i == len(x) - 1:
    print(f'{numero} es capicua')
else:
    print(f'{numero} no es capicua')