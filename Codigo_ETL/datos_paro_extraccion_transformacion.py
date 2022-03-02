# IMPORTAMOS LAS LIBRERIAS NECESARIAS
import os
import pandas as pd

# DEFINICION DE FUNCIONES QUE NOS SERAN DE UTILIDAD
def paro_hombres(row):
    paro_hombres = int(row['Paro hombre edad < 25']) + int(row['Paro hombre edad 25 -45']) + int(row['Paro hombre edad >=45'])
    return paro_hombres

def paro_mujeres(row):
    paro_mujeres = int(row['Paro mujer edad < 25']) + int(row['Paro mujer edad 25 -45']) + int(row['Paro mujer edad >=45'])
    return paro_mujeres

def sep_mes(row):
    mes = row['mes'].split()[0]
    return mes

def sep_ano(row):
    ano = row['mes'].split()[2]
    return ano

def remove_special_characters(df):
    # Create dictionary with special characters and its replacements
    elements_to_replace_dict = {'á':'a','é':'e','í':'i','ó':'o','ú':'u','ñ':'n','à':'a','è':'e','ì':'i','ò':'o','ù':'u','\'':'',',':'','ü':'u'}
    df = df.replace({'Comunidad Autonoma': elements_to_replace_dict}, regex=True)
    df = df.replace({'Provincia': elements_to_replace_dict}, regex=True)
    df = df.replace({'Municipio': elements_to_replace_dict}, regex=True)
    # Return resulting dataframe
    return df


# INICIO DEL PROCESO DE EXTRACCIÓN
# CARGA DE LOS DATOS EN ARCHIVOS CSV A TABLAS DE PANDAS
tabla_paro_2006 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2006_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2007 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2007_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2008 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2008_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2009 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2009_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2010 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2010_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2011 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2011_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2012 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2012_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2013 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2013_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2014 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2014_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2015 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2015_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2016 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2016_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2017 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2017_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2018 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2018_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2019 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2019_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2020 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2020_csv.csv', sep= ";", header=1, encoding='latin-1')
tabla_paro_2021 = pd.read_csv('DATOS_PARO_POR_MUNICIPIO\Paro_por_municipios_2021_csv.csv', sep= ";", header=1, encoding='latin-1')

tablas_paro = [tabla_paro_2006,tabla_paro_2007,tabla_paro_2008,tabla_paro_2009,tabla_paro_2010,tabla_paro_2011,tabla_paro_2012,tabla_paro_2013,tabla_paro_2014,tabla_paro_2015,
               tabla_paro_2016,tabla_paro_2017,tabla_paro_2018,tabla_paro_2019,tabla_paro_2020,tabla_paro_2021]

datos_paro = pd.concat(tablas_paro)
# FIN PROCESO DE EXTRACCION

# INICIO PROCESO DE TRANSFORMACION
# COMPROBAMOS SI HAY VALORES PERDIDOS (NULOS)
#print(datos_paro.isnull().values.any())    # NO HAY VALORES PERDIDOS
datos_paro = datos_paro.rename(columns={' Municipio':'Municipio', 'Código mes ':'Codigo mes', 'Código de CA':'Codigo de CA', 'Comunidad Autónoma':'Comunidad Autonoma',
                                        'Paro Construcción':'Paro Construccion', 'Paro hombre edad 25 -45 ':'Paro hombre edad 25 -45', 'Paro mujer edad 25 -45 ':'Paro mujer edad 25 -45'})
datos_paro["Paro Hombres"] = datos_paro.apply(lambda row: paro_hombres(row), axis=1)
datos_paro["Paro Mujeres"] = datos_paro.apply(lambda row: paro_mujeres(row), axis=1)
datos_paro["anualidad"] = datos_paro.apply(lambda row: sep_ano(row), axis=1)
datos_paro["mes"] = datos_paro.apply(lambda row: sep_mes(row), axis=1)
datos_paro = remove_special_characters(datos_paro)
print(datos_paro)
datos_paro.to_csv('datos_intermedios.csv', sep=';', index=False)




