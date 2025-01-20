# 1º Haz un programa que lea dos palabras y que indique el orden lexicográfico. 
# Escribe en un línea indicando si a<b, a>b o a=b.
# Ejemplo: a = Anna, b = Javier, Anna < Jabier. 

a = input("a: ")
b = input("b: ")

if a < b:
    print(f"{a} < {b}")
elif a > b:
    print(f"{a} > {b}")
else: 
    print(f"{a} = {b}")
    