# IMPORTAMOS LAS LIBRERIAS NECESARIAS
import os
import pandas as pd

def paro(row,tabla_paro):
    mask_t = tabla_paro['Codigo mes'] == row['Codigo mes']
    mask_CA = tabla_paro['Comunidad Autonoma'] == row['Comunidad Autonoma']
    mask_Pr = tabla_paro['Provincia'] == row['Provincia']
    mask_Mun = tabla_paro['Municipio'] == row['Municipio']
    result_df = tabla_paro.loc[mask_CA & mask_Mun & mask_Pr & mask_t]
    if row['ID_SEXO'] == 0:
        if row['ID_RANGO'] == 0:
            return result_df['Paro mujer edad < 25']
        elif row['ID_RANGO'] == 1:
            return result_df['Paro mujer edad 25 -45']
        elif row['ID_RANGO'] == 2:
            return result_df['Paro mujer edad >=45']        
    elif row['ID_SEXO'] == 1:
        if row['ID_RANGO'] == 0:
            return result_df['Paro hombre edad < 25']
        elif row['ID_RANGO'] == 1:
            return result_df['Paro hombre edad 25 -45']
        elif row['ID_RANGO'] == 2:
            return result_df['Paro hombre edad >=45']  
            


# CARGA DE LOS DATOS EN ARCHIVOS CSV A TABLAS DE PANDAS
tabla_paro = pd.read_csv('datos_intermedios.csv', sep= ";", header=0, encoding='latin-1')

tiempo_dimension = tabla_paro.drop_duplicates(['Codigo mes','mes','anualidad'])[['Codigo mes','mes','anualidad']]

lugares_dimension = tabla_paro.drop_duplicates(['Comunidad Autonoma','Provincia','Municipio'])[['Comunidad Autonoma','Provincia','Municipio']]

sexo_dimension = pd.DataFrame({'ID_SEXO':[0,1],'SEXO_STRING':['Hombre','Mujer']})

#sector_dimension = pd.DataFrame({'ID_SECTOR':[0,1,2,3,4],'SECTOR':['Paro Agricola','Paro Industria','Paro Construccion','Paro Servicio','Paro Sin Empleo Anterior']})

edad_dimension = pd.DataFrame({'ID_RANGO':[0,1,2],'RANGO':['Edad < 25','Edad 25-45','Edad >= 45']})

tabla_paro_hechos = tabla_paro[['Codigo mes','Comunidad Autonoma','Provincia','Municipio']]
tabla_paro_hechos = pd.merge(tabla_paro_hechos,sexo_dimension['ID_SEXO'], how="cross")
tabla_paro_hechos = pd.merge(tabla_paro_hechos,edad_dimension['ID_RANGO'], how="cross")
lista_no_aplanada = tabla_paro[['Paro hombre edad < 25','Paro hombre edad 25 -45','Paro hombre edad >=45','Paro mujer edad < 25',
                                  'Paro mujer edad 25 -45','Paro mujer edad >=45']].values.tolist()

lista_aplanada = [item for l in lista_no_aplanada for item in l]

tabla_paro_hechos['PARO'] = lista_aplanada
tabla_paro_hechos.to_csv('tabla_hechos.csv', sep=';' ,index=False)
print(tabla_paro_hechos)

"""
tabla_paro_hechos = pd.merge(tiempo_dimension['Codigo mes'],lugares_dimension, how="cross")
tabla_paro_hechos = pd.merge(tabla_paro_hechos,sexo_dimension['ID_SEXO'], how="cross")
tabla_paro_hechos = pd.merge(tabla_paro_hechos,edad_dimension['ID_RANGO'], how="cross")



lista_no_aplanada = tabla_paro[['Paro hombre edad < 25','Paro hombre edad 25 -45','Paro hombre edad >=45','Paro mujer edad < 25',
                                  'Paro mujer edad 25 -45','Paro mujer edad >=45']].values.tolist()

lista_aplanada = [item for l in lista_no_aplanada for item in l]

tabla_paro_hechos['PARO'] = lista_aplanada
tabla_paro_hechos.to_csv('tabla_hechos.csv', sep=';', index=False)
"""
""""
tabla_paro_hechos['PARO'] = tabla_paro_hechos.apply(lambda row: paro(row,tabla_paro), axis=1)
print(tabla_paro_hechos)
tabla_paro_hechos.to_csv('tabla_hechos.csv', sep=';', index=False)
"""
