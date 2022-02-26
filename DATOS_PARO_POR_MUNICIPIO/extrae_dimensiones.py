# IMPORTAMOS LAS LIBRERIAS NECESARIAS
import os
import pandas as pd

# CARGA DE LOS DATOS EN ARCHIVOS CSV A TABLAS DE PANDAS
tabla_paro = pd.read_csv('datos_intermedios.csv', sep= ";", header=0, encoding='latin-1')

tiempo_dimension = tabla_paro.drop_duplicates(['Codigo mes','mes','anualidad'])[['Codigo mes','mes','anualidad']]
tiempo_dimension.to_csv('dimension_tiempo.csv', sep=';', index=False)

lugares_dimension = tabla_paro.drop_duplicates(['Comunidad Autonoma','Provincia','Municipio'])[['Comunidad Autonoma','Provincia','Municipio']]
lugares_dimension.to_csv('dimension_lugares.csv', sep=';', index=False)

sexo_dimension = pd.DataFrame({'ID_SEXO':[0,1],'SEXO_STRING':['Hombre','Mujer']})
sexo_dimension.to_csv('dimension_sexo.csv', sep=';', index=False)

edad_dimension = pd.DataFrame({'ID_RANGO':[0,1,2],'RANGO':['Edad < 25','Edad 25-45','Edad >= 45']})
edad_dimension.to_csv('dimension_edad.csv', sep=';', index=False)

