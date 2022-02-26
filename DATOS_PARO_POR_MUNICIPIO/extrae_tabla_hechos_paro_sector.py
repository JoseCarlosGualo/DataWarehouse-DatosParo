# IMPORTAMOS LAS LIBRERIAS NECESARIAS
import os
import pandas as pd

# CARGA DE LOS DATOS EN ARCHIVOS CSV A TABLAS DE PANDAS
tabla_paro = pd.read_csv('datos_intermedios.csv', sep= ";", header=0, encoding='latin-1')

tiempo_dimension = tabla_paro.drop_duplicates(['Codigo mes','mes','anualidad'])[['Codigo mes','mes','anualidad']]

lugares_dimension = tabla_paro.drop_duplicates(['Comunidad Autonoma','Provincia','Municipio'])[['Comunidad Autonoma','Provincia','Municipio']]

sector_dimension = pd.DataFrame({'ID_SECTOR':[0,1,2,3,4],'SECTOR':['Paro Agricola','Paro Industria','Paro Construccion','Paro Servicio','Paro Sin Empleo Anterior']})

tabla_paro_hechos = tabla_paro[['Codigo mes','Comunidad Autonoma','Provincia','Municipio']]
tabla_paro_hechos = pd.merge(tabla_paro_hechos,sector_dimension['ID_SECTOR'], how="cross")
lista_no_aplanada = tabla_paro[['Paro Agricultura','Paro Industria','Paro Construccion','Paro Servicios',
                                  'Paro Sin empleo Anterior']].values.tolist()

lista_aplanada = [item for l in lista_no_aplanada for item in l]

tabla_paro_hechos['PARO'] = lista_aplanada
tabla_paro_hechos = tabla_paro_hechos.rename(columns={'Codigo mes':'ID_TIEMPO'})
tabla_paro_hechos.to_csv('tabla_hechos_paro_por_sector.csv', sep=';' ,index=False)
print(tabla_paro_hechos)