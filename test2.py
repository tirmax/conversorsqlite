#librerias
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#conexion
conexion=sqlite3.connect("jptdatabase.db")

#cursor
consulta=conexion.cursor()

#consultar
df =pd.read_sql_query("SELECT * FROM sqlite_sequence",conexion)

#se crea el excel
df.to_excel('jptdatabase.xlsx', index=False)
print(df)
print("excel creado")

#crear grafica
datos=pd.read_excel('jptdatabase.xlsx')
df=pd.DataFrame(datos)

df.groupby('name')['seq'].sum().plot(kind='barh',legend='Reverse')
plt.xlabel('otros datos')
print("grafica creada")


#Cerramos
conexion.close()

