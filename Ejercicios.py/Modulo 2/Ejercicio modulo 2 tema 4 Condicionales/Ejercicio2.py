# 2º Haz un programa que lea y que indique por pantalla si es una mayúscula, 
# si es una minúscula, si es una vocal y si es una consonante. 

letra = input("Escriba una letra: ")

if letra =="a" or letra =="e" or letra =="i" or letra =="o" or letra =="u":
    print(f"{letra} Es vocal")
elif letra =="A" or letra =="E" or letra =="I" or letra =="O" or letra =="U":
    print(f"{letra} Es vocal")
else: 
    print(f"{letra} Es consonante")

if letra.islower():
    print(f"{letra} Es minúscula")
else:
    print(f"{letra} Es mayuscula")