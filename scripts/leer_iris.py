import pandas as pd

#Leer el archivo CSV y crear un DataFrame
df = pd.read_csv("datos/iris.csv", header=None)

#Corregir nombres de columnas
df.columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"]

#Mostrar información del DataFrame por consola
print("Primeras filas: ")
print(df.head())

print()

print("Dimensiones del dataset: ")
print(df.shape)

print()

print("Información general")
df.info()

print()

print("Resumen estadístico:")
print(df.describe())