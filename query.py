#%%
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv, find_dotenv
from os import environ

load_dotenv(find_dotenv())

user = environ.get("SQLSERVER_USER")
password = environ.get("SQLSERVER_PASS")

#%%
engine = sqlalchemy.create_engine("mssql+pyodbc://user:password@./ETL_PRD?driver=SQL Server")

pedidos = pd.read_sql(sql="SELECT * FROM fato_pedidos", con=engine)
produtos = pd.read_sql(sql="SELECT * FROM dim_produtos", con=engine)
lojas = pd.read_sql(sql="SELECT * FROM dim_lojas", con=engine)

#%%

produtos[pedidos['loja'] == '1']['valor'].sum().round(2)






# %%
