# Diccionarios:

# 1. Haz un programa que convierta dos listas en un diccionario.

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
diccionario = {}

for dato in range(0, len(lista1)):
    diccionario[lista1[dato]] = lista2[dato]

print(diccionario)

# 2. Haz un programa que fusione dos diccionarios de Python en uno solo.

diccionario1 = {"a": "alfa",
                "b": "beta",
                "c": "charli",
                "d": "delta"}
diccionario2 = { "uno": 1,
                "dos": 2,
                "tres": 3,
                "cuatro": 4}

for clave,valor in diccionario2.items():
    diccionario1[clave] = valor

print(diccionario1)

# 3. Haz un programa que imprima el valor de la clave 'history' del siguiente diccionario.

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
                }}}}

print(sampleDict["class"]["student"]["marks"]["history"])

# 4. Haz un programa que inicialice el diccionario con valores por defecto.

diccionario = {"lugar": "casa",
               "metros": "25 m"}
valores_por_defecto = ["Madrid", "Barcelona"]
resultado = dict.fromkeys(valores_por_defecto, diccionario) # lo miré, no me salio.

print(resultado)

# 5. Haz un programa que cree un diccionario extrayendo las claves de un diccionario dado.

diccionario = {"producto": "coche",
               "precio": "300000 $",
               "cuotas": 10}
claves = ["producto", "precio",]
resultado = dict()

for valor in claves:
    resultado.update({valor: diccionario[valor]}) # ¿No deberia ser ({->valor<-: diccionario[valor]}) y no ->claves<-?

print(resultado)

# 6. Haz un programa que elimine una lista de claves de un diccionario.

diccionario = {"coche": "toyota",
               "vivienda": "piso",
               "perro": "labrador",
               "trabajo": "programacion"}
claves = ["vivienda", "trabajo"]

for clave in claves:
    if clave in diccionario:
        del diccionario[clave]

print(diccionario)

# o mejor:
diccionario = {"coche": "toyota",
               "vivienda": "piso",
               "perro": "labrador",
               "trabajo": "programacion"}
claves = ["vivienda", "trabajo"]

for clave in claves:
    diccionario.pop(clave) 

print(diccionario)

# 7. Haz un programa que compruebe si un valor existe en un diccionario.

diccionario = {"uno": 1,
               "dos": 2,
               "tres": 3,
               "cuatro": 4,
               "cinco": 5}
valor = int(input("Ingresa un valor: "))

if valor in diccionario.values():
    print(f"{valor} existe en el diccionario.")
else: 
    print(f"{valor} no existe en el diccionario")

# 8. Haz un programa que cambie el nombre de la clave de un diccionario.

diccionario = {"coche": "toyota",
               "vivienda": "piso",
               "perro": "labrador",
               "trabajo": "programacion"}
diccionario["profecion"] = diccionario.pop("trabajo")

print(diccionario)

# 9. Haz un programa que obtenga la clave de un valor mínimo del siguiente diccionario.

sample_dict = {'Physics': 82,
               'Math': 65,
               'history': 75}

print(f"{min(sample_dict)}: {min(sample_dict.values())}")

# 10. Haz un programa que cambie el valor de una clave en un diccionario anidado.

diccionario = {"casa1":{"baños": 2,
                        "salon": 1,
                        "habitacion": 1},
               "casa2":{"baños": 3,
                        "salon": 1,
                        "habitacion": 2}}
diccionario["casa2"]["habitacion"] = 3

print(diccionario)

# SETS:

# 1. Haz un programa que añada una lista de elementos a un conjunto.

conjunto = {1, 2, 3, 4, 5, 6}
lista = [6, 7, 8, 9, 10]

conjunto.update(lista)

print(conjunto)

# 2. Haz un programa que devuelva un nuevo conjunto de elementos idénticos de dos conjuntos.

conjunto1 = {"a", "b", "c", "d"}
conjunto2 = {"c", "d", "e", "f"}

print(conjunto1.intersection(conjunto2))

# 3. Haz un programa que obtenga sólo elementos únicos de dos conjuntos.

conjunto1 = {"a", "b", "c", "d"}
conjunto2 = {"c", "d", "e", "f"}

print(conjunto1.union(conjunto2))


# 4. Haz un programa que actualice el primer conjunto con elementos que no existen en el segundo conjunto.

conjunto1 = {"a", "b", "c", "d"}
conjunto2 = {"c", "d", "e", "f"}

conjunto1.difference_update(conjunto2)

print(conjunto1)


# 5. Haz un programa que elimine elementos del conjunto a la vez.

conjunto = {"a", "b", "c", "d", "e", "f"}

conjunto.difference_update("a", "c", "e")

print(conjunto)

# 6. Haz un programa que devuelva un conjunto de elementos presentes en el conjunto A o B, pero no en ambos.

conjunto1 = {"a", "b", "c", "d"}
conjunto2 = {"c", "d", "e", "f"}

print(conjunto1.symmetric_difference(conjunto2))

# conjunto1.symmetric_difference(conjunto2) ¿por qué así me da los dos primero valores de cada conjunto?
# print(conjunto1)

# 7. Haz un programa que compruebe si dos conjuntos tienen algún elemento en común. En caso afirmativo,
# mostrar los elementos comunes.

conjunto1 = {"a", "b", "c", "d"}
conjunto2 = {"c", "d", "e", "f"}

if conjunto1.isdisjoint(conjunto2):
     print("No hay valores iguales en los conjuntos")
else: 
    print(conjunto1.intersection(conjunto2))

# 8. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos comunes.

conjunto1 = {"a", "b", "c", "d"}
conjunto2 = {"c", "d", "e", "f"}

conjunto1.symmetric_difference_update(conjunto2)

print(conjunto1)


# 9. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos comunes.

conjunto1 = {"a", "b", "c", "d"}
conjunto2 = {"c", "d", "e", "f"}

conjunto1.intersection_update(conjunto2)

print(conjunto1)