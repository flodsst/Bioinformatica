import pandas as pd

df = pd.read_csv("datos/iris.csv", header=None)

df.columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"]

print(df.head())
print(df.shape)
print(df.columns)