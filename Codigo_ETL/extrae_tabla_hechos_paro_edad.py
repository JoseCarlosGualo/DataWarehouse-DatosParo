# IMPORTAMOS LAS LIBRERIAS NECESARIAS
import os
import pandas as pd

# CARGA DE LOS DATOS EN ARCHIVOS CSV A TABLAS DE PANDAS
tabla_paro = pd.read_csv('datos_intermedios.csv', sep= ";", header=0, encoding='latin-1')

tiempo_dimension = tabla_paro.drop_duplicates(['Codigo mes','mes','anualidad'])[['Codigo mes','mes','anualidad']]

lugares_dimension = tabla_paro.drop_duplicates(['Comunidad Autonoma','Provincia','Municipio'])[['Comunidad Autonoma','Provincia','Municipio']]

sexo_dimension = pd.DataFrame({'ID_SEXO':[0,1],'SEXO_STRING':['Hombre','Mujer']})

edad_dimension = pd.DataFrame({'ID_RANGO':[0,1,2],'RANGO':['Edad < 25','Edad 25-45','Edad >= 45']})

tabla_paro_hechos = tabla_paro[['Codigo mes','Comunidad Autonoma','Provincia','Municipio']]
tabla_paro_hechos = pd.merge(tabla_paro_hechos,sexo_dimension['ID_SEXO'], how="cross")
tabla_paro_hechos = pd.merge(tabla_paro_hechos,edad_dimension['ID_RANGO'], how="cross")
lista_no_aplanada = tabla_paro[['Paro hombre edad < 25','Paro hombre edad 25 -45','Paro hombre edad >=45','Paro mujer edad < 25',
                                  'Paro mujer edad 25 -45','Paro mujer edad >=45']].values.tolist()

lista_aplanada = [item for l in lista_no_aplanada for item in l]

tabla_paro_hechos['PARO'] = lista_aplanada
tabla_paro_hechos = tabla_paro_hechos.rename(columns={'Codigo mes':'ID_TIEMPO'})
tabla_paro_hechos.to_csv('tabla_hechos_paro_por_rango_edad.csv', sep=';' ,index=False)
print(tabla_paro_hechos)