# 3º Haz un programa que lea un entero que representa una tempratura en grados Celcius, y que diga si hace calor,
# si hace frío, o si se está bien. Suponed que hace calor si la temperatura es mayor de 30 grados, que hace frio 
# si es meor de 10 grados y que esta bien en otro caso. 

temperatura = int(input("¿A cuantos grados estamos?: "))

if temperatura > 30:
    print("Hace calor.")
elif temperatura < 10:
    print("Hace frio.")
else: 
    print("Esta bien.")