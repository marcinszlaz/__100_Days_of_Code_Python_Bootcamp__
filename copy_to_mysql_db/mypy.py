from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import pandas

load_dotenv()
# create an engine
engine = create_engine(f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
# druk = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
# us = os.getenv('DB_USER')
# ps = os.getenv('DB_PASSWORD')
# hs = os.getenv('DB_HOST')
# nm = os.getenv('DB_NAME')
# po = os.getenv('DB_PORT')
# print(f'user:{us}\npassword:{ps}\nhostname:{hs}\ndb_name:{nm}\nport:{po}')
# print(druk)
# engine = create_engine(f'mysql+mysqlconnector://winuser:winuser@10.215.14.30:3306/covid')
#
#
df1 = pandas.read_excel('data/CovidDeaths.xlsx', engine='openpyxl' )
df2 = pandas.read_excel('data/CovidVaccinations.xlsx', engine='openpyxl')
df1.to_sql('CovidDeaths',if_exists='append',con=engine)
df2.to_sql('CovidVaccinations',con=engine)
# print(df1)
# print(df2)