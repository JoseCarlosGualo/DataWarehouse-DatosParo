# IMPORTAMOS LAS LIBRERIAS NECESARIAS
import os
import pandas as pd

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

print(datos_paro)
print(datos_paro.isnull().values.any())