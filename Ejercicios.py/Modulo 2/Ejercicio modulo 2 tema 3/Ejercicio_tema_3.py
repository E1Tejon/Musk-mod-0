# 1º Haz un programa que lea un número decimal por pantalla, lo convierta a entero y lo imprima. 

Num1 = float(input("introduzca un número decimal: "))

print(int(Num1))

# 2º Haz un programa que lea un número decimal por pantalla e imprima su tipo y su valor redondeado en la misma lista. 

Num2 = float(input("introduzca un número decimal: "))

print("Tipo:{} Redondeo: {}".format(type(Num2), round(Num2)))

# 3º Haz un programa que lea dos número por pantalla e imprima su diferencia en valor absoluto. 

num1 = float(input("Introduzca un número: "))
num2 = float(input("Introduzca otro número: "))
diferencia = abs(num1 - num2)

print(f"La diferencia entre {num1} y {num2} es {diferencia}")