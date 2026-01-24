from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

# create an engine
engine = create_engine(f'mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD)')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}')

with open(file='book_data.sql',mode='r',encoding='utf-8') as file:
  sql_script = file.read().split(';')
sql_script_clean = [line.replace('\t','').replace('\n','').strip() for line in sql_script if line.strip()]
# print(sql_script)
# print(sql_script_clean)


with engine.connect() as connection:
  for one_line in sql_script_clean:
    connection.execute(text((one_line)))
  connection.commit()

print('Wykonano skrypt')