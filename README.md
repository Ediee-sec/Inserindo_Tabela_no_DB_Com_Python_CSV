## Incluindo tabela no SQL Server apartir de um arquivo CSV com Python.

> Nesta documentação irei explicar como inserir dados em um banco de dados apartir de um arquivo CSV.

> Irei utilizar o `SQLAlchemy` como conector ao banco de dados, mas poderia ser qualquer outra que tem por objetivo de se conectar ao DB

> Neste artigo não irei fazer nenhuma transformação no arquivo csv, apenas irei extrair os dados e carrega-los no banco de dados

----

* **Linguagem de Programação**
>`Python 3.6` *ou superior*
* **Bibliotecas**
>`SQLAlchemy` `Pandas` `urllib`
* **Install**
>`pip install SQLAlchemy` `pip install pandas`
* **Imports**
> `from sqlalchemy import create_engine` 
>`import pandas as pd` 
>`import urllib`
* **LINK do arquivo CSV**
> [Dados de infrações de trânsito Setembro/2022](http://dados.df.gov.br/dataset/3a3b7b40-c715-439d-9dff-f22b47fc5994/resource/c2f74b4c-8597-43d9-83fc-66e102423ec4/download/dados-abertosset2022.csv)

---


### **Mapa do código**

1. **Função que cria a conexão com o banco de dados**

```python
def conn_database():
    params = urllib.parse.quote_plus(
        "DRIVER={SQL SERVER};"
        "SERVER=EMERSON-PEREIRA\SQLEXPRESS;"
        "DATABASE=LOCADORA;"
        "trusted_connection=yes"
    )

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}", echo=True)

```
2. **Função que importa o arquivo csv para a memória**

```python
def import_csv():
    df = pd.read_csv('dados-abertosset2022.csv',delimiter=';',encoding='utf-8')

    return df
```

3. **Função que cria a tabela no banco de dados com os dados do arquivo csv**

```python
def export_data():
    import_csv().to_sql('TB_NEW',con=conn_database(), if_exists='replace', index=False, chunksize=10000)
```

4. **Executa o programa**

```python
export_data()
```

