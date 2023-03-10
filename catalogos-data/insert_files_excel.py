from lxml import etree
import pandas as pd
import os
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from pdb import set_trace


catalogs_description_fix = ['TipoDocumento-2.1.gc']
#catalogs_invalid_fix = ['TiposEventos.gc']
con_string = "host='localhost' dbname='catalogos' user='superuser' password='superuser123'"


def get_pathfiles():
    p = '/home/mhurtado/catalogos_API/api/v1/catalogos/Listas de valores'
    _fixed_list = []
    print('Archivos = ' + str(len(os.listdir(p))))
    for file in os.listdir(p):
        full_path = os.path.join(p, file)#Create the full path to .gc file
        if os.path.isfile(full_path):#if the path is actually a file
            _fixed_list.append(full_path)#Create a fixed list with the paths
    return _fixed_list#Return the paths
     


def load_files():
    #file_list = get_pathfiles()
    #print(str(len(file_list)) + ' archivos leidos')
    #for file in file_list:
        file = '/home/mhurtado/yezdo-co/catalagos-api/codigopostal.xlsx'
        filename  = os.path.basename(file)
        print('IMPORTANDO\n')
        print(filename + '\n')
        try:
            print('Running')
            print('Opened')

            #set_trace()

            df = pd.read_excel(
                file,
                sheet_name=0,
                header=None,
                skiprows=1,
                names=['codigo_departamento','nombre_departamento',
                    'codigo_municipio','nombre_municipio','name','tipo'],
            )
            print(df)

            table_name = filename.removesuffix('.xlsx')  
            table_name = table_name.lower()
            print('TABLA : ' + table_name)
            
            
            #set_trace()
            SQLALCHEMY_DATABASE_URL = 'postgresql://yezdo:Mahr1119;.@0.0.0.0:5432/catalogos_db'
            db = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
            #db.execute('TRUNCATE TABLE {} RESTART IDENTITY'.format(table_name))
            meta = MetaData()

            table = Table(
                  table_name, meta,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('codigo_departamento', String),
                  Column('nombre_departamento', String),
                  Column('codigo_municipio', String),
                  Column('nombre_municipio', String),
                  Column('name', String),
                  Column('tipo', String)
             )

            meta.create_all(db)

            df.to_sql(
               table_name,
               con = db,
               schema='public',
               if_exists='append',
               index=False,
               )
            

        except etree.XMLSyntaxError as e:
            print('catalogo: '+ filename + ' XMLSyntaxError\n')
            print('catalogo:'+ filename +' '+str(e))
            #continue
        except Exception as e:
            print('catalogo: '+ filename+'\n')
            print('catalogo:'+ filename +' '+str(e))
            #continue

load_files()
