# 5º Haz un programa que indique si un año es bisiesto o no. Un año bisiesto tiene 366 días. 
# Después de la reforma gregoriana, los años bisiestos son los múltipos de cuatro que no acaban en dos 0,
# y también los acabados en dos 0 tales que el número que queda después de sacar los dos 0 finales es 
# divisible por 4. Así, 1800 y 1900, a pesar de ser múltiples de cuatro, no fueran bisiestos; en cambio,
# 2000 lo fue. 

fecha = int(input("Fecha: "))

if fecha % 4 == 0 and (fecha % 100 != 0 or fecha % 400 ==0): # No supe como evitar que 2000 fuera bisiesto.
    print(f"{fecha} es un año bisiesto")
else: 
    print(f"{fecha} es un año no bisiesto")
