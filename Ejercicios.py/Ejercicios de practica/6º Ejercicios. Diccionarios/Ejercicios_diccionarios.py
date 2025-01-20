# Un diccionario es una colección de tipos de datos emparejados ( Clases: valor) modificables ( matables )
# desordenados.
# Crear un diccionario: ( se crea con {} )

diccionario = {"nombre": "Che", # Clave : Valor
               "edad": 31,
               "población": "Tenerife",
               "casado": False,
               "deportes": ["MMA", "judo","boxeo"],
               "hermano": {"nombre": "Samuel",
                            "edad": 29,
                            "población": "Tenerife"}
               }

# Ver la longitud:

print(len(diccionario))

# Acceder a los elementos:

print(diccionario["deportes"]) # NO se nombra la posición, se indica el nombre de la clave.
print(diccionario["hermano"]["nombre"]) # se entra en un diccionario dentro de otro con claves entre corchetes.
print(diccionario["deportes"][0]) #se entra en una lista dentro de un diccionario con la posición entre corchetes.

# Modificar valores:

diccionario["edad"] = 32 # Solo se modifican valores, para cambiar una clave se elimina y se crea otra.
print(diccionario["edad"])

diccionario["comprometido"] = False # se agrega una clave con un valor nuevo en la última posición y NO lo modifica.
print(diccionario["comprometido"])

diccionario.update({"población": "Canarias"}) # Tambien se puede usar .update 
print(diccionario["población"])

# Añadir elementos:

diccionario["codigo postal"] = 33333
print(diccionario["codigo postal"])

print("----------------------------")

# Eliminar pares de clave y valor de un diccionario:
#    pop(clave): elimina el elemento con el nombre de la clave especificada:

diccionario.pop("nombre") # borra la clave y el valor si introdicimos la clave.
print(diccionario)

años = diccionario.pop("edad") # podemos guardar un valor de una clave que borremos en una variable.
print(años)

deporte = diccionario["deportes"].pop(0) # para guardar en una variable un valor que borremos
print(deporte)                           # de una lista en un diccionario.

deporte_2 = diccionario.pop("deportes")[0] # tambien se puede hacer así.
print(deporte_2)

#    popitem(): elimina el último elemento. 

diccionario.popitem()
print(diccionario)

#    del: elimina un elemento con el nombre de clave especificado:

del diccionario["casado"]
print(diccionario)

print("-----------------------------")

# Acceder a las claves:

claves = diccionario.keys() # Nos devuelve las keys en formato lista
print(claves)

#Acceder a los valores:

valores = diccionario.values()
print(valores)

# Bucles "for" con diccionarios:

print(diccionario.items()) # Te da el diccionario en "listas de tuplas", clave y valor. ([()])

for dato in diccionario: 
    print(dato) # Solo devuelve las claves.

for clave,valor in diccionario.items():
    print(f"clave: {clave}, valor: {valor}") # nos devuelve las claves y valores. 
    
for clave in diccionario.keys(): # devuelve las claves como el 1º bucle.
    print(clave)
    
for valor in diccionario.values(): # devuelve los valores. 
    print(valor)

# EJERCICIOS:

# 1º Crea un diccionario vacio y llamalo perro

perro = {}

# 2º Agregue nombre, color, raza, patas y edad al diccionario de perro

perro["nombre"] = "toto"
perro["color"] = "negro"
perro["raza"] = "mil leches"
perro["patas"] = 4
perro["edad"] = 11

print(perro)

# 3º Obtener la longitud del diccionario perro

print(len(perro))

# 4º Agrega una clave "abilidades" como una lista

perro["habilidades"] = ["correr", "saltar",]
print(perro)

# 5º Obten el valor de las habilidades y verifica el tipo de dato, debería ser una lista. 

habilidades = perro["habilidades"]
print("habilidades: ", perro["habilidades"])
print(type(habilidades))
print(type(perro["habilidades"]))