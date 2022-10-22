from sqlalchemy import create_engine
import pandas as pd
import urllib


def conn_database():
    params = urllib.parse.quote_plus(
        "DRIVER={SQL SERVER};"
        "SERVER=EMERSON-PEREIRA\SQLEXPRESS;"
        "DATABASE=LOCADORA;"
        "trusted_connection=yes"
    )

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}", echo=True)

    return engine

def import_csv():
    df = pd.read_csv('dados-abertosset2022.csv',delimiter=';',encoding='utf-8')

    return df

def export_data():
    import_csv().to_sql('TB_NEW',con=conn_database(), if_exists='replace', index=False, chunksize=10000)

export_data()



