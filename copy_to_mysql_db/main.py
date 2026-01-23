from sqlalchemy import create_engine, text

# create an engine
engine = create_engine('mysql+pymysql://winuser:winuser@10.215.14.30:3306/book_shop')

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