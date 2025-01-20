# 17º  Haz un programa que lea varias descripciones de rectángulos y de círculos, 
# y que para cada una escriba el área correspondiente. La entrada empieza con un número n, 
# seguido de n descripciones. Si es de un rectángulo, se tiene la palabra “rectángulo” seguida
# de dos reales estrictamente positivos que indican la longitud y la anchura. Si es de un círculo,
# se tiene la palabra “círculo” seguida de un real estrictamente positivo que indica el radio.

secuencia = int(input("¿Cuántas áreas vamos a calcular?: "))

for x in range(0, secuencia):
    figura = input("Figura: ")
    area = 0
    
    if figura == "rectangulo" or figura == "cuadrado":
        largo = float(input("Longitud en cm: "))
        ancho = float(input("Anchura en cm: "))
        area = largo * ancho
        print(f"El {figura} tiene área de {area} cm.")
    elif figura == "circulo":
        radio = float(input("Radio:"))
        area = pow(radio,2) * 3.141592 
        print(f"El {figura} tiene área de {area} cm.")
