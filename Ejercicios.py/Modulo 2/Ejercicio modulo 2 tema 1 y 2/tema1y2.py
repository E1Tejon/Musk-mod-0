# 1º Haz un programa que escriba una línea con el mensaje: "¡Buenos días a todo el mundo!".

print("¡Buenos días a todo el mundo!")

# 2º Haz un programa que declare tres palabras a, b y c, que se escriba una línea con c, b y a en este orden. 

a = "estas?"
b = "¿como"
c = "hola,"

print(c, b, a)

# 3º Haz un programa que declare dos números y que escriba la suma. 

num1 = 5
num2 = 4 

print(f"{num1} + {num2} = {num1 + num2}")

# 4º Haz un programa que declare dos números y que escriba el máximo. 

x = 2
y = 3

print(max(x, y))

# 5º Haz un programa que declare tres números, todos diferentes y que escriba el máximo.

núm1 = 10
núm2 = 100
núm3 = 1

print(max(num1, núm2, núm3))

# 6º Haz un programa que dado un valor calcule su cuadrado y sucubo.

número = 12

cuadrado = pow(número, 2)
cubo = pow(número, 3)

print(cuadrado)
print(cubo)

# 7º Haz un programa que devuelva el valor absoluto de un número. 

X = -36

print(abs(X))

# 8º Haz un programa que lea dos numerales A y B, con B>0, y que escriba la división entera (d) y el residuo (r)
# de A entre B. Recordar que por definición, (d) y (r) tienen que ser los únicos enteros tales que: 0 ≤ r < b 
# y: d * B + r = A. 

A = 33
B = 2
d = A // B
r = A % B

print(f"Dividendo: {A}. Divisor: {B}. Cociente: {d}. Residuo: {r}")

# 9º Haz un programa que, dada la cantidad de segundos, diga cuantas horas, minutos y segundos representan.

Segundos = int(input("segundos: "))
Minutos = Segundos / 60
Horas = Minutos / 60

print(f"{Segundos} segundos son: {Minutos} minutos, que son {Horas} horas")

# 10º Haz un programa que dada una temperatura en grados Celsius la muestre en grados Fahrenheit y en grados Kelvin.
# (F = 1.8 * C + 32 y K = C + 273)

C = int(input("temperatura: "))
F = 1.8 * C + 32
K = C + 273

print(f"Estamos a {C} Grados centigrados, que son: {F} grados Fahrenheit, o {K} grados Kelvin")