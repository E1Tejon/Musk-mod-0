# Listas: es una colección ordenada y modificable. Permite miembros duplicados. Admite cualquier tipo de dato.

# 1º Crear listas:

my_list = [1,2,3]
otra_lista = list[1,2,3]

# 2º Como acceder a los elemenos de una lista: 

colores =["verde", "rojo", "azul", "blanco", "negro"]
#            0        1       2        3        4
# Para acceder al primer elemento se empieza en 0:

print(colores[0]) # verde.
print(colores[2]) # azul. 

# Para acceder al ultimo elemento se empieza en -1:

print(colores[-2]) # blanco.

# 3º Modificar un elemento de la lista:

colores =["verde", "rojo", "azul", "blanco", "negro"]

colores[0] = "amarillo"
print(colores) # Lista con amarillo por verde entre comillas con comas y todas las variables seguidas.

for color in colores:
    print(color) # Lista variable por variable separadas y sin comillas.

# 4º Comprobación de elementos en una lista: 
    # Verificar un elemento si es miembro de una lista usando el operador "in". Vea el ejemplo a continuación:

colores =["verde", "rojo", "azul", "blanco", "negro"]
existe = "rojo" in colores

print(existe)

for color in colores:
    if color == "rojo":
        print("rojo")

# 5º Longuitud de lista: con "len()" vemos la longitud de la lista, siempre empieza a contar en 1. 

colores =["verde", "rojo", "azul", "blanco", "negro"]

print(len(colores)) # imprime 5. 

# 6º Anadir un nuevo elemento:
    # Con el metodo "append()" añadimos el elemento al final de la lista. 

colores =["verde", "rojo", "azul", "blanco", "negro"]
colores.append("naranja")

print(colores)

    # Con el metodo "insert()", añadimos el elemento en una posición en concreto. 

colores =["verde", "rojo", "azul", "blanco", "negro"]

colores.insert(2, "violeta") # Posición que ocupara seguida de la variable a insertar.

print(colores)

# 7º Eliminar elementos de una lista:
# 7.1 El método "remove" elimina un elemento específico de una lista. 

colores =["verde", "rojo", "azul", "blanco", "negro"]
colores.remove("rojo")

print(colores)

# 7.2 El metodo "pop()" elimina el indice especificado o el último elemento si no se especifica el índice. 

colores =["verde", "rojo", "azul", "blanco", "negro"]
colores.pop(0) # El indice empieza en 0.

print(colores)

# 7.3 El metodo "del" eliminas por completo el elemento.

colores =["verde", "rojo", "azul", "blanco", "negro"]
del colores[0] # Se elimina verde de la base de datos.

print(colores)

# 8º Contar elementos en una lista: 
    # El método "count()" devuelve el número de veces que aparece un elemento en una lista: 

colores =["verde", "rojo", "azul", "blanco", "negro"]

print(colores.count("azul")) # devuelve el número de repeticiones. 

# 9º Invertir la lista:
    # El método "reverse()" invierte el orden de la lista. 

colores =["verde", "rojo", "azul", "blanco", "negro"]
colores.reverse()

print(colores)

# 10º Ordenar elementos de la lista:
    # Para ordenar listas podemos usar el método "sort()" o las funciones integradas "sorted()". 
    # sort(): este metodo modifica la lista original. 
colores =["verde", "rojo", "azul", "blanco", "negro"]
colores.sort() 

print(colores)

# 10.1 El método "sort()" reordena los elementos de la lista en orden ascendente y modifica la lista original.
    # Si un argumento del método "sort()" inverso es igual a verdadero, organizara la lista en orden descendente. 

colores =["verde", "rojo", "azul", "blanco", "negro"]
colores.sort(reverse = True)
 
print(colores)

    # sorted(): devuelve la lista ordenada sin modificar la lista original.

colores =["verde", "rojo", "azul", "blanco", "negro"]
colores_ordenados = sorted(colores)
# O directamente:
print(sorted(colores))

    # Se puede usar el reverse: 

colores =["verde", "rojo", "azul", "blanco", "negro"]
colores_ordenados =sorted(colores, reverse = True)
# O directamente:
print(sorted(colores, reverse = True))

# 11º Cortar elementos de una lista:
    # Podemos especificar un rango de índices positivos especificando el inicio,
    # el final y el salto, el valor de retorno será una nueva lista. 
    # (valores predeterminados para inicio = 0, fin = len(lst) -1 (último elemento), salto = 1).

fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4] # El primero donde empieza y el el segundo donde acaba partiendo de 0. 
all_fruits = fruits[0:] # Acaba en el último. 
orange_mango = fruits[1:3] # De un elemento a otro. 
orange_mango_lemon = fruits[1:]
orange_lemon = fruits[ : :2] # De principio a fin de 2 en 2. (principio: fin: saltos). 

# 12º Listas de listas (matrices):

matriz =[[1,2,3,4], [11,12,13,14]]

    # Aqui accedemos a la primera sublista. 
    
print(matriz[0]) # Devuelve la primera lista.
    
    # Aqui accedemos a elementos de la primera sublista. 
    
print(matriz[0][1]) # Nos devuelve el 2º elemento de la primera lista.


# TUPLES: 

# Una tupla es una colección de diferentes tipos de datos que está ordenada y es inmutable.
# Las tuplas se escriben entre corchetes, (). Una vez creada una tupla, no podemos cambiar suus valores.
# No podemos usr métodos agregar,insertar o eliminar en una tupla porque no es modificable.
# A diferencia de la lista, la tupla tiene pocos métodos. Métodos relacionados con tuplas: 

# "tupla()": para crear una tupla vacía.
# "count()": para contar el número de un elemento específico en una tupla.
# "index()": para encontrar el índice de un elemento específico en una tupla.

# 1º Creando una tupla:

mi_tupla = (1,2,3,4)

# 2º Longitud de tupla:
    # Usamos el método "len()" para obtener la longitud de una tupla.

print(len(mi_tupla))

# 3º Accediendo a elemento de tuplas. 
    
print(mi_tupla[0]) # Devuelve el primero de la tupla.
    
# 4º Contar tuplas:
    # Podemos dividir una subtupla fespecificando un rango de índices donde comenzar y 
    # dónde terminar en la tupla; el valor de retorno será ina nueva tupla con los elementos especificados. 

mi_tupla[1:2] # Devuelve 2 y 3. 

# 5º Cambiar tuplas a lista:
    # Podemos cambiar tuplas a listas y listas a tuplas. La tupla es inmutable,
    # si queremos modificar una tupla debemos combiarla a una lista.
    
mi_lista = list(mi_tupla) # De tupla a lista.
print(type(mi_lista)) # imprime el tipo de dato, en este caso una clase lista. 

mi_lista.append(5) # Añadimos un elemento a la lista.

mi_tupla = tuple(mi_lista) # De lista a tupla.
print(type(mi_tupla)) # imprime el tipo de dato, en este caso una clase tuple. 

# 6º Comprobar un elemento en una tupla: 
    #Podemos verificar si un elemento existe o no en una tupla usando "in", devuelve un valor booleano. 

existe = 5 in mi_tupla

print(existe)

for tupla in mi_tupla:
    if tupla == 5:
        print(5)

# 7º Eliminar tuplas:
   # No es posible eliminar un solo elemento en una tupla, pero es posible eliminar la tupla misma usando "del": 

del mi_tupla


# EJERCICIOS:

# 1º Declara una lista vacia: 

lista = []

print(lista)

# 2º Declara una lista co 7 elementos:

lista = [1,2,3,4,5]

# 3º Encontrar la longitud de esa lista:

lista = [1,2,3,4,5,6]

print(len(lista))

# 4º Corta tu lista, muestra los dos primeros elementos y luego los dos últimos:
    # Cortando la lista en dos y quedandonos con el primero y ultimo de cada lista:

lista = [1,2,3,4,5,6]
lista_1 = lista[:3]
lista_2 = lista[3:]

print(f"{lista_1[0]} y {lista_2[0]}")
print(f"{lista_1[2]} y {lista_2[2]}")

    # Cortando la lista por los dos extremos: 

lista = [1,2,3,4,5,6]
comienzo = lista[:2]
final = lista[4:]

print(comienzo)
print(final)

# 5º Obten el 1º elemento de la lista, el elemento del medio y el último de la lista: 

lista = [1,2,3,4,5,6]
mitad = int(len(lista)//2)-1

print(lista[0])
print(lista[mitad])
print(lista[-1])

# 6º Suma de elementos: Escribe un programa que sume todos los elementos de una lista de números enteros. 

lista = [2, 3, 6, 1, 4, 30]
suma = 0

for numero in lista:
    suma += numero

print(suma)

