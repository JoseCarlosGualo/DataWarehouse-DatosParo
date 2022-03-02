import pymysql
import pandas as pd

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='sys'
        )
        
        self.cursor = self.connection.cursor()
        print("Conexión establecida exitosamente")

tiempo_dimension = pd.read_csv('dimension_tiempo.csv', sep= ";", header=0, encoding='latin-1')

lugar_dimension = pd.read_csv('dimension_lugares.csv', sep= ";", header=0, encoding='latin-1')

sexo_dimension = pd.read_csv('dimension_sexo.csv', sep= ";", header=0, encoding='latin-1')

tiempo_dimension = pd.read_csv('dimension_tiempo.csv', sep= ";", header=0, encoding='latin-1')

sector_dimension = pd.read_csv('dimension_sector.csv', sep= ";", header=0, encoding='latin-1')

edad_dimension = pd.read_csv('dimension_edad.csv', sep= ";", header=0, encoding='latin-1')

hechos_sector = pd.read_csv('tabla_hechos_paro_por_sector.csv', sep= ";", header=0, encoding='latin-1')
hechos_sector = hechos_sector.loc[1:2000,['ID_TIEMPO','Comunidad Autonoma','Provincia','Municipio','ID_SECTOR','PARO']]
hechos_edad = pd.read_csv('tabla_hechos_paro_por_rango_edad.csv', sep= ";", header=0, encoding='latin-1')
hechos_edad = hechos_edad.loc[1:2000,['ID_TIEMPO','Comunidad Autonoma','Provincia','Municipio','ID_SEXO','ID_RANGO','PARO']]

database = DataBase()


database.cursor.execute("CREATE TABLE dimension_sexo (id_sexo INT PRIMARY KEY, sexo_string VARCHAR(255))")
database.cursor.execute("CREATE TABLE dimension_edad (id_rango INT PRIMARY KEY, rango_string VARCHAR(255))")
database.cursor.execute("CREATE TABLE dimension_sector (id_sector INT PRIMARY KEY, sector_string VARCHAR(255))")
database.cursor.execute("CREATE TABLE dimension_lugar (id_ca VARCHAR(255), id_provincia VARCHAR(255), id_municipio VARCHAR(255), PRIMARY KEY (id_ca, id_provincia, id_municipio))")
database.cursor.execute("CREATE TABLE dimension_tiempo (id_tiempo INT PRIMARY KEY, mes VARCHAR(255), anualidad VARCHAR(255))")
database.cursor.execute("CREATE TABLE hechos_sector (id_tiempo INT, id_ca VARCHAR(255), id_provincia VARCHAR(255), id_municipio VARCHAR(255), id_sector INT, paro INT, PRIMARY KEY (id_tiempo, id_ca, id_provincia, id_municipio, id_sector))")
database.cursor.execute("CREATE TABLE hechos_edad (id_tiempo INT, id_ca VARCHAR(255), id_provincia VARCHAR(255), id_municipio VARCHAR(255), id_rango_edad INT, id_sexo INT, paro INT, PRIMARY KEY (id_tiempo, id_ca, id_provincia, id_municipio, id_rango_edad, id_sexo))")

for row in sexo_dimension.index:
    
    database.cursor.execute('INSERT INTO dimension_sexo(id_sexo, \
          sexo_string)' \
          'VALUES({}, \'{}\')'.format(sexo_dimension["ID_SEXO"][row],sexo_dimension["SEXO_STRING"][row]))
    
for row in edad_dimension.index:
    
    database.cursor.execute('INSERT INTO dimension_edad(id_rango, \
          rango_string)' \
          'VALUES({}, \'{}\')'.format(edad_dimension["ID_RANGO"][row],edad_dimension["RANGO"][row]))

for row in sector_dimension.index:
    
    database.cursor.execute('INSERT INTO dimension_sector(id_sector, \
          sector_string)' \
          'VALUES({}, \'{}\')'.format(sector_dimension["ID_SECTOR"][row],sector_dimension["SECTOR"][row]))
    
for row in lugar_dimension.index:
    
    database.cursor.execute('INSERT INTO dimension_lugar(id_ca, \
          id_provincia, id_municipio)' \
          'VALUES(\'{}\',\'{}\',\'{}\')'.format(lugar_dimension["Comunidad Autonoma"][row],lugar_dimension["Provincia"][row],lugar_dimension["Municipio"][row]))

for row in tiempo_dimension.index:
    
    database.cursor.execute('INSERT INTO dimension_tiempo(id_tiempo, \
          mes, anualidad)' \
          'VALUES(\'{}\',\'{}\',\'{}\')'.format(tiempo_dimension["ID_TIEMPO"][row],tiempo_dimension["mes"][row],tiempo_dimension["anualidad"][row]))

for row in hechos_sector.index:
    
    database.cursor.execute('INSERT INTO hechos_sector(id_tiempo, \
          id_ca, id_provincia, id_municipio, id_sector, paro)' \
          'VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(hechos_sector["ID_TIEMPO"][row],hechos_sector["Comunidad Autonoma"][row],hechos_sector["Provincia"][row],
                                                                     hechos_sector["Municipio"][row],hechos_sector["ID_SECTOR"][row],hechos_sector["PARO"][row]))

for row in hechos_edad.index:
    
    database.cursor.execute('INSERT INTO hechos_edad(id_tiempo, \
          id_ca, id_provincia, id_municipio, id_rango_edad, id_sexo, paro)' \
          'VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(hechos_edad["ID_TIEMPO"][row],hechos_edad["Comunidad Autonoma"][row],hechos_edad["Provincia"][row],
                                                                            hechos_edad["Municipio"][row],hechos_edad["ID_SEXO"][row],hechos_edad["ID_RANGO"][row],
                                                                            hechos_edad["PARO"][row]))

database.cursor.execute('ALTER TABLE hechos_edad \
    ADD FOREIGN KEY (id_tiempo) REFERENCES dimension_tiempo(id_tiempo);')

database.cursor.execute('ALTER TABLE hechos_edad \
    ADD FOREIGN KEY (id_ca, id_provincia, id_municipio) REFERENCES dimension_lugar(id_ca, id_provincia, id_municipio);')

"""database.cursor.execute('ALTER TABLE hechos_edad \
    ADD FOREIGN KEY (id_sexo) REFERENCES dimension_sexo(id_sexo);')"""

database.cursor.execute('ALTER TABLE hechos_edad \
    ADD FOREIGN KEY (id_rango_edad) REFERENCES dimension_edad(id_rango);')


database.cursor.execute('ALTER TABLE hechos_sector \
    ADD FOREIGN KEY (id_tiempo) REFERENCES dimension_tiempo(id_tiempo);')

database.cursor.execute('ALTER TABLE hechos_sector \
    ADD FOREIGN KEY (id_ca, id_provincia, id_municipio) REFERENCES dimension_lugar(id_ca, id_provincia, id_municipio);')

database.cursor.execute('ALTER TABLE hechos_sector \
    ADD FOREIGN KEY (id_sector) REFERENCES dimension_sector(id_sector);')

#close the connection to the database.
database.connection.commit()
database.cursor.close()