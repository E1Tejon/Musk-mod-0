# Ejercicios Módulo 5:

# Tema 1: Manejo de Archivos

# 1º Escribe una función en python para leer el conjunto de un archivo de texto "poema.txt"
# línea por línea y mostrar el mismo en pantalla. 

with open ("poema.txt", "w", encoding = "utf-8") as archivo:
    archivo.write ("""Que es mi barco, mi tesoro,
                   que es mi dios, la libertad,
                   mi ley, la fuerza y el viento, 
                   mi unica patria la mar."""
                   )

with open ("poema.txt", "r", encoding = "utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

# 2º Escribe una función para contar el número de líneas de un archivo de texto "historia.txt": 
# Ejemplo: Si el archivo "story.txt" contiene las siguientes líneas:
# Un niño está jugando allí.
# Hay un parque infantil. 
# Un avión está en el cielo. 
# El cielo es rosa.
# La contraseña puede contener letras y números. El resultado debe ser 5.

with open ("story.txt", "w", encoding = "utf-8") as texto:
    texto.write ("""Un niño está jugando allí.
                   Hay un parque infantil. 
                   Un avión está en el cielo. 
                   El cielo es rosa."""
                   )
    
with open("story.txt", "r", encoding = "utf-8") as texto:
        lineas = texto.readlines()
        print(f"el archivo tiene: {len(lineas)} lineas.")

# 3º Escribe una función en Python para contar y mostrar el número total 
# de palabras en un archivo de texto.

def contar_palabras(nombre):
    try:
        with open(nombre,"r", encoding = "utf-8") as texto:
            contenido = texto.read()
            palabras = contenido.split()
            return len(palabras)
    except FileNotFoundError:
        print(f"el archivo {texto} no fue encontrado")
        return 0
numero_palabras = contar_palabras("story.txt")
print(f"El archivo contiene {numero_palabras} palabras.")

# 4º Escriba una función para leer líneas de un archivo de texto "notas.txt". 
# Su función debe encontrar y mostrar la aparición de la palabra "el". 

def contar_el(nombre_archivo, palabra_buscada):
    try:
        with open(nombre_archivo,"r", encoding = "utf-8") as archivo:
            contenido = archivo.read()
            palabras = contenido.lower().split()
            return palabras.count(palabra_buscada.lower())
    except FileNotFoundError:
        print(f"{nombre_archivo} no se encuentra")
        return 0

with open("notas.txt","w", encoding = "utf-8") as archivo:
    archivo.write("""El cielo esta enladrillado,
                  quien lo desenladrillara,
                  el primer desenladrillador
                  que lo desenladrille,
                  buen desenladrillador sera.""")

nombre_archivo = "notas.txt"
palabra_clave = "el"
repeticiones = contar_el(nombre_archivo, palabra_clave)
print(f"{palabra_clave} se repite {repeticiones} en {nombre_archivo}.")

# 5º Escriba una función display_words() en python para leer las lineas de 
# un archivo de texto "story.txt", y mostrar aquellas palabras que tengan 
# menos de 4 caracteres. 

def display_words(nombre_archivo):
    try:
        with open(nombre_archivo,"r", encoding = "utf-8") as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            palabras_4 = [palabra for palabra in palabras if len(palabra) < 4]
            print(", ".join(palabras_4))
    except FileNotFoundError:
        print(f"{nombre_archivo} no se encuentra.")

display_words("story.txt")

# 6º Un archivo de texto llamado "materia.txt" contiene algún texto, que necesita
# ser mostrado de manera que cada carácter siguiente esté separado por un símbolo "#".
# Escriba una definición de función para hash_display() en Python que muestre 
# todo el contenido del archivo matter.txt en el formato deseado.
# Ejemplo: Si el archivo materia.txt tiene el significado almacenado: 
# EL MUNDO ES REDONDO
# La función hash_display()debería mostrar el siguiente contenido:
# T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#

def hash_display(nombre_archivo):
    try:
        with open(nombre_archivo,"r", encoding ="utf-8") as archivo:
            contenido = archivo.read()
            formato_hash = "#".join(contenido.strip())
            print(formato_hash)
    except FileNotFoundError:
        print(f"{nombre_archivo} no encontrado.")

with open("materia.txt","w", encoding ="utf-8") as archivo:
    archivo.write("EL MUNDO ES REDONDO")
hash_display("materia.txt")

# 7º Escribe un programa en Python para generar 26 archivos de texto 
# llamados A.txt, B.txt, y así sucesivamente hasta Z.txt.

def generar_archivos():
    alfabeto = ("A","B","C","D","E","F",
                "G","H","I","J","K","L",
                "M","N","O","P","Q","R",
                "S","T","U","V","W","X",
                "Y","Z")
    for letra in alfabeto:
        nombre_archivo = f"{letra}.txt"
        with open(nombre_archivo,"w", encoding = "utf-8")as archivo:
            archivo.write(f"{letra}.\n")
        print(f"{nombre_archivo}")
        
generar_archivos()

# 8º Escribe un programa en python para añadir texto a un archivo y mostrar
# el texto en python.txt

def agregar_mostrar_texto(nombre_archivo,agregar_texto):
    with open(nombre_archivo,"a", encoding ="utf-8") as archivo:
        archivo.write(agregar_texto + "\n")
    with open(nombre_archivo, "r", encoding ="utf-8") as archivo:
        contenido = archivo.read()
        print(f"{nombre_archivo}:\n{contenido}")
nombre_de_archivo = "python.txt"
nuevo_texto = "Hola Mundo"
agregar_mostrar_texto(nombre_de_archivo, nuevo_texto)

# 9º Escribe un programa en python para calcular la frecuencia de todas las 
# palabras de un archivo txt.

from collections import Counter

def calcular_frecuencia(nombre_archivo):
    try:
        with open(nombre_archivo,"r", encoding ="utf-8") as archivo:
            contenido = archivo.read()
            palabras = contenido.lower().split()
            frecuencias = Counter(palabras)
            print(nombre_archivo)
            for palabra, frecuencia in frecuencias.items():
                print(f"{palabra} : {frecuencia}")
    except FileNotFoundError:
        print(f"{nombre_archivo} no encontrado.")

calcular_frecuencia("story.txt")

# 10º Escribe un programa en python para comprobar si un archivo especificado existe. 

import os

def verificar_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        print(f"{nombre_archivo} Existe.") 
    else: 
        print(f"{nombre_archivo} No existe.")

verificar_archivo("story.txt")
verificar_archivo("No_existe.txt")

# Tema 2: Introducción a JSON.

# 1º Para realizar los ejercicios usar el archivo csvAutomobile_data.csv.
# A partir del conjunto de datos dado, imprime las cinco primeras y últimas filas. 

import pandas as pd 

def mostrar_filas(nombre_archivo):
    try:
        datos = pd.read_csv(nombre_archivo)
        print("Primeras filas:")
        print(datos.head())
        print("\nUltimas filas:")
        print(datos.tail())
    except FileNotFoundError:
        print(f"{nombre_archivo} no es encuentra.")

mostrar_filas("Modulo5_Automobile_data.csv")

# 2º Limpia el conjunto de datos y actualiza archivos CSV. Reemplaza todos los valalores
# de las columnas que tengan ?, n.a, o NaN.

import pandas as pd 

def limpiar_datos(nombre_archivo, nuevo_archivo):
    try:
        datos= pd.read_csv(nombre_archivo)
        datos.replace(["?","n.a","NaN"], pd.NA, inplace = True)
        datos.fillna(0,inplace = True)
        datos.to_csv(nuevo_archivo, index = False)
        print(f"{nuevo_archivo} limpio.")
    except FileNotFoundError:
        print(f"{nuevo_archivo} no se encuentra.")
    except Exception as e: 
        print(f"Error: {e}")

archivo_original = "Modulo5_Automobile_data.csv"
archivo_limpio = "Modulo5_Automobile_data_limpio.csv"
limpiar_datos(archivo_original, archivo_limpio)
print(pd.read_csv(archivo_limpio))

# 3º Encuentra el nombre de la empresa del coche más caro. Imprime el nombre de
# la empresa del coche más caro y su precio.

import pandas as pd 

def mas_caro(nombre_archibo):
    try:
        datos = pd.read_csv(nombre_archivo)
        max_precio = datos.loc[datos["price"].idxmax()]
        empresa =  max_precio["company"]
        precio =  max_precio["price"]
        print(f"Empresa: {empresa}, Precio: {precio}")
    except FileNotFoundError:
        print(f"{nombre_archibo} no encontrado")
    except Exception as e: 
        print(f"Error: {e}")

nombre_archivo = "Modulo5_Automobile_data.csv"
mas_caro(nombre_archivo)

# 4º Imprime todos los datos de los coches Toyota.

import pandas as pd 

def coches_toyota(nombre_archivo):
    try:
        datos = pd.read_csv(nombre_archivo)
        toyotas = datos[datos["company"].str.lower() == "toyota"]
        if not toyotas.empty:
            print(toyotas)
        else: 
            print("No hay Toyotas")
    except FileNotFoundError:
        print(f"{nombre_archivo} no se encuentra.")
    except Exception as e: 
        print(f"Error: {e}")

nombre_archivo = "Modulo5_Automobile_data.csv"
coches_toyota(nombre_archivo)

# 5º Cuenta el total de coches por empresa.

import pandas as pd 

def coches_por_empresa(nombre_archivo):
    try:
        datos = pd.read_csv(nombre_archivo)
        conteo = datos["company"].value_counts()
        print("Coches por empresa:")
        print(conteo)
    except FileNotFoundError:
        print(f"{nombre_archivo} no se encuentra.")
    except Exception as e: 
        print(f"Error: {e}")

nombre_archivo = "Modulo5_Automobile_data.csv"
coches_por_empresa(nombre_archivo)

# 6º Encuentra el coche con el precio más alto de
# precios de cada empresa. 

import pandas as pd 

def mas_caro_por_empresa(nombre_archivo):
    try:
        datos = pd.read_csv(nombre_archivo)
        datos["price"] = pd.to_numeric(datos["price"],errors ="coerce")
        caros = datos.loc[datos.groupby("company")["price"].idxmax()]
        print(caros[["company","body-style","price"]])
    except FileNotFoundError:
        print(f"{nombre_archivo} no se encuentra.")
    except Exception as e: 
        print(f"Error: {e}")

nombre_archivo = "Modulo5_Automobile_data.csv"
mas_caro_por_empresa(nombre_archivo)

# 7º Encuentra el kilometraje medio de cada empresa
# fabricante de automóviles. 

import pandas as pd 

def kilometraje_empresas(nombre_archivo):
    try:
        datos = pd.read_csv(nombre_archivo)
        kilometraje = datos.groupby("company")["average-mileage"].mean()
        print("kilopmetrajes medios: ")
        print(kilometraje)
    except FileNotFoundError:
        print(f"{nombre_archivo} no se encuentra.")
    except Exception as e: 
        print(f"Error: {e}")

nombre_archivo = "Modulo5_Automobile_data.csv"
kilometraje_empresas(nombre_archivo)

# 8º Ordena todos los coches por la columna Precio.

import pandas as pd 
def ordenar_precios(nombre_archivo):
    try:
        datos = pd.read_csv(nombre_archivo)
        orden = datos.sort_values(by ="price", ascending = True)
        orden = datos.groupby("company")["price"].mean()
        print("Orden por precios:")
        print(orden)
    except FileNotFoundError:
        print(f"{nombre_archivo} no se encuentra.")
    except Exception as e: 
        print(f"Error: {e}")

nombre_archivo = "Modulo5_Automobile_data.csv"
ordenar_precios(nombre_archivo)

# 9º Concatena dos dataframes utilizando las siguientes condiciones:
# GermanCars = {'Company':['Ford','Mercedes','BMV','Audi'],'Price':[23845, 171995, 135925, 71400]} 
# japaneseCars = {'Company':['Toyota','Honda','Nissan','Mitsubishi'],'Price':[29995, 23600, 61500, 58900]}

import pandas as pd 

def concatenador_dataframes(data1, data2):
    df_data1 = pd.DataFrame(data1)
    df_data2 =pd.DataFrame(data2)
    df_concatenado = pd.concat([df_data1, df_data2], ignore_index = True)
    print(df_concatenado)

GermanCars = {'Company':['Ford','Mercedes','BMV','Audi'],
    'Price':[23845, 171995, 135925, 71400]} 
japaneseCars = {'Company':['Toyota','Honda','Nissan','Mitsubishi'],
                'Price':[29995, 23600, 61500, 58900]}

concatenador_dataframes(GermanCars, japaneseCars)

# 10º Combina dos dataframe utilizando la siguente condición. 
# Crea dos dataframe utilizando los siguientes dos Dict, fusiónalos 
# y añade el segundo dataframe como una nueva columna al prinmer dataframe.
# Car_Price = {"Company":["Toyota","Honda","BMV","Audi"], "Price": [23845, 17995,135925, 71400]}
# Car_Horsepower ={"Company":["Toyota","Honda","BMV","Audi"], "horsepower":[141, 80, 182, 160]}

import pandas as pd 

def concatenador(data1, data2):
    df_data1 = pd.DataFrame(data1)
    df_data2 =pd.DataFrame(data2)
    df_concatenado = pd.merge(df_data1, df_data2, on = "Company")
    print(df_concatenado)

Car_Price ={"Company":["Toyota","Honda","BMV","Audi"],
             "Price": [23845, 17995,135925, 71400]}
Car_Horsepower ={"Company":["Toyota","Honda","BMV","Audi"], 
                 "horsepower":[141, 80, 182, 160]}

concatenador(Car_Price, Car_Horsepower)

# Tema 3: Introducción a Pandas

# 1º Crea un array de enteros 4x2 e imprime sus atributos. 
# Nota: El elemento debe ser de tipo unsignedint16. Imprime los siguientes atributos:
# La shapedel array.
# Las dimensiones del array. 
# El tamaño de cada elemento del array en bytes. 

import pandas as pd 

array = pd.DataFrame([[0,0],[0,0],[0,0],[0,0]], dtype = "uint16")
print("shapedel:", array.shape)
print("dimensiones:", array.ndim)
print("tamaño", array.dtypes.apply(lambda x: x.itemsize).iloc[0])

# 2º Crea una matriz de enteros 5x2 de un rango entre 100 y 200 tal que
# la diferencia entre cada elemento sea 10. 

import pandas as pd 

rango = list(range(100 ,200 ,10))
matriz = pd.DataFrame([rango[e:e+2] for e in range(0, len(rango), 2)])
print("matriz:",matriz)

# 3º A continuación se muestra el array Numpy proporcionado. Devuelve un array de elementos
# tomando la tercera columna de todas las filas. 
# sampleArray = numpy.array([[11,22,33],[44,55,66],[77,88,99]])

import numpy as np 

sampleArray = np.array([[11,22,33],
                        [44,55,66],
                        [77,88,99]])
columna3 = sampleArray[:,2]
print(columna3)

# 4º Devuelve un array de filas impares y columnas pares dado el siguiente array: 
# sampleArray = numpy.array([[3,6,9,12],[15,18,21,24],[27,30,33,36],[39,42,45,48],[51,54,57,60]])

import numpy as np 

sampleArray = np.array([[3,6,9,12],
                        [15,18,21,24],
                        [27,30,33,36],
                        [39,42,45,48],
                        [51,54,57,60]])
filas_impares = sampleArray[1::2] 
columnas_pares = sampleArray[0::2]
print(filas_impares)
print(columnas_pares)

# 5º Crea una matriz de resultados sumando las siguientes dos matrices de NumPy.
# A continuación. modifica la matriz de resultados calculando el cuadrado de cada elemento.  
# arrayOne = numpy.array([[5, 6, 9],[21, 18, 27]])
# arrayTwo = numpy.array([[15, 33, 24],[4, 7, 1]])

import numpy as np 

arrayOne = np.array([[5, 6, 9],
                     [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24],
                     [4, 7, 1]])

matriz_resultante = arrayOne + arrayTwo
matriz_resultante_cuadrado = np.square(matriz_resultante)
print(matriz_resultante)
print(matriz_resultante_cuadrado)

# 6º Divide la matriz en cuatro submatrices de igual tamaño. 
# Nota: Crea una matriz de enteros 8x3 de un rango entre 10 y 34 de
# tal manera que la diferencia entre cada elemento sea 1 y luego 
# divide la matriz en cuanto submatrices de igual tamaño. 

import numpy as np 

matriz = np.arange(10, 34).reshape(8, 3)
submatriz = np.vsplit(matriz, 4)
print("Matriz:")
print(matriz)
for m, submatrices in enumerate(submatriz):
    print(f"\nsubmatrices{m+1}:")
    print(submatrices)
    
# 7º Ordena el siguiente array de NumPy:
# Caso1: Ordenar el array por la segunda fila. 
# Caso2: Ordena el array por la segunda columna. 
# sampleArray = numpy.array([[34, 43, 73],[82, 22, 12],[53, 94, 66]])

import numpy as np 

sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])
por_filas = sampleArray[:, sampleArray[1].argsort()]
por_columnas = sampleArray[sampleArray[:, 1].argsort()]
print("\nCaso 1:")
print(por_filas)
print("\nCaso 2:")
print(por_columnas)

# 8º Imprime el máximo del eje 0 y el mínimo del eje 1
# de la siguiente matriz bidimensional:
# sampleArray = numpy.array([[34, 43, 73],[82, 22, 12],[53, 94, 66]])

import numpy as np 

sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])
maximo_eje0 = np.max(sampleArray, axis = 0)
minimo_eje1 = np.min(sampleArray, axis = 1)
print("\nMáximo por columnas:")
print(maximo_eje0)
print("\nMínimo por filas:")
print(minimo_eje1)

# 9º Elimina a la segunda columna de una matriz dada
# e inserta la siguiente columna nueva en su lugar. 
# sampleArray = numpy.array([[34, 43, 73],[82, 22, 12],[53, 94, 66]])
# newColumn = numpy.array([[10, 10, 10]])

import numpy as np 

sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])
newColumn = np.array([10, 10, 10])
sin_columna2 = np.delete(sampleArray, 1, axis = 1)
nueva_matriz = np.insert(sin_columna2, 1, newColumn, axis = 1)
print("\nNueva matriz")
print(nueva_matriz)

# Tema 4: Librerias adicionales: Numpy. 

# 1º Para resolver estos ejercicios debes usar el fichero csvcompany_sales_date.csv. 
# Lee el beneficio total de todos los meses y muéstralo mediante un gráficode líneas. 
# Se proporcionan los datos de beneficio total de cada mes. El gráfico de líneas 
# generado debe incluir las siguientes propiedades:
# Nombre de la etiqueta X = Número de mes
# Nombre de la etiqueta Y = Beneficio total

import pandas as pd 
import matplotlib.pyplot as plt 

company = pd.read_csv("Modulo5_company_sales_data.csv")
company.plot(x = "month_number",
         y ="total_profit",
         marker = "o", 
         linestyle = "-",
         color = "g",
         label = "Benefico total")
plt.xlabel("Meses", fontsize = 12)
plt.ylabel("Beneficio total", fontsize = 12)
plt.title("Grafico de beneficios mensuales", fontsize = 15)
plt.show()

# 2º Obtenga el beneficio total de todos los meses y muestre un gráfico de
# líneas con las siguientes propiedades de estilo: 
# Estilo de línea punteada y el color de la línea debe ser rojo.
# Mostrar la leyenda en la parte inferior derecha. 
# Nombre de la etiqueta X =Número de mes. 
# Nombre de la etiqueta y = Número de unidades vendidas. 
# Añadir un marcador de círculo. 
# El ancho de la línea debe ser 3. 

import pandas as pd 
import matplotlib.pyplot as plt 

company = pd.read_csv("Modulo5_company_sales_data.csv")
company.plot(x = "month_number",
         y ="total_profit", 
         linestyle = ":",
         color = "r",
         marker = "o",
         linewidth = 3,
         label = "Benefico total")
plt.xlabel("Meses", fontsize = 12)
plt.ylabel("Beneficio total", fontsize = 12)
plt.title("Gráfico de beneficios mensuales", fontsize = 15)
plt.legend(loc = "lower right")
plt.show()

# 3º Lee todos los datos de ventas de productos y mostrarlos mediante un gráfico multilínea. 
# Muestra el número de unidades vendidas por mes para cada producto utilizando gráficos
# multilínea.(es decir, una línea de trazado separada para cada producto). 

import pandas as pd 
import matplotlib.pyplot as plt 

company = pd.read_csv("Modulo5_company_sales_data.csv")
productos = ["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]
colores = ["blue","orange","green","red","purple","brown"]
for producto, color in zip(productos, colores):
    plt.plot(company["month_number"], company[producto], label = producto)
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.title("Ventas por mes")
plt.show()

# 4º Lee los datos de las ventas de pasta de dientes de cada mes y muéstralos mediante un 
# gráfico de dispersión (scatter). Además, añade una cuadrícula en el gráfico. El estilo de
# la cuadrícula debe ser "-". 

import pandas as pd 
import matplotlib.pyplot as plt 

company = pd.read_csv("Modulo5_company_sales_data.csv")
pasta_dental = company["toothpaste"]
plt.scatter(company["month_number"], pasta_dental, color = "r", label = "Pasta de dientes")
plt.grid(linestyle ="-")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.title("Ventas mensuales de pasta de dientes")
plt.show()

# 5º Lee los datos de ventas de los productos creama facial y lavado de cara y muestralos 
# mediante el gráfico barras. El gráfico de barras debe mostrar el número de unidades vendidas
# por mes para cada producto. Añade de una barra distinta para cada producto en el mismo gráfico. 

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

company = pd.read_csv("Modulo5_company_sales_data.csv")
meses = company["month_number"].values
crema_facial = company["facecream"].values
lavado_de_cara = company["facewash"].values 
ancho_barra = 0.4
x = np.arange(len(meses))
plt.bar(x - ancho_barra/2, crema_facial, ancho_barra, label = "Crema facial", color ="blue")
plt.bar(x + ancho_barra/2, lavado_de_cara, ancho_barra, label = "lavado de cara", color ="orange")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.title("Comparación de ventas mensuales")
plt.xticks(x, meses)
plt.grid(True, linestyle = "--", which ="both", axis ="both", color = "gray", linewidth = 0.2)
plt.show()

# 6º Lee los datos de ventas de jabón de baño de todos los meses y muértralos mediante un gráfico
# de barras. Guarda este gráfico en tu disco duro.

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

company = pd.read_csv("Modulo5_company_sales_data.csv")
meses = company["month_number"].values
jabon = company["bathingsoap"].values 
plt.bar(meses, jabon, color = "blue")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.title("Ventas mensuales de jabón")
plt.xticks(meses)
plt.savefig("ventas_jabon.png")
plt.show()

# 7º Lee el beneficio total de cada mes y muéstralos
# utilizando el histograma para ver los rangos de 
# beneficio más comunes. 

import pandas as pd 
import matplotlib.pyplot as plt

company = pd.read_csv("Modulo5_company_sales_data.csv")
beneficio = company["total_profit"].values 
plt.hist(beneficio, bins = "auto", color = "b")
plt.xlabel("Beneficios")
plt.ylabel("Frecuencia")
plt.title("Rangos de veneficios")
plt.show()

# 8º Calcula los datos de ventas totales del último año
# para cada producto y muéstralos mediante un gráfico circular.
# Nota: En el gráfiico circular muestra el número de unidades 
# vendidas por año para cada producto en porcentaje. 

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

company = pd.read_csv("Modulo5_company_sales_data.csv")
productos = company.columns[1:-2]
ventas = np.array([company[producto].sum() for producto in productos])
porcentaje = (ventas/ventas.sum())*100
plt.figure(figsize = (8, 8))
plt.pie(porcentaje,
        labels = productos,
        autopct = lambda p: f"{p:.1f}%")
plt.title("Porcentajes de ventas")
plt.show()

# 9º Lee el jabón de baño de todos los meses y visualízalo utilizando el Subplot. 

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

company = pd.read_csv("Modulo5_company_sales_data.csv")
meses = company["month_number"].values
jabon = company["bathingsoap"].values 
lavado_de_cara = company["facewash"].values 
plt.subplot(2, 1, 1)
plt.plot(meses,
        jabon,
        marker = "o",
        color = "b",
        linestyle = "-")
plt.title("Ventas de jabón")
plt.xlabel("meses")
plt.ylabel("Unidades")
plt.xticks(meses)
plt.subplot(2, 1, 2)
plt.plot(meses,
        lavado_de_cara,
        marker = "o",
        color = "r",
        linestyle = "-")
plt.title("Ventas de lavado de cara")
plt.xlabel("meses")
plt.ylabel("Unidades")
plt.xticks(meses)
plt.tight_layout()
plt.show()

# 10º Lee todos los datos de las ventas de productosy muéstralos mediante el diagrama de pila. 

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

company = pd.read_csv("Modulo5_company_sales_data.csv")
meses = company["month_number"].values
productos = company.columns[1:-2]
ventas = company[productos].values
plt.stackplot(meses,
              ventas.T,
              labels = productos)
plt.xlabel("meses")
plt.ylabel("Ventas")
plt.title("Ventas mensuales")
plt.show()