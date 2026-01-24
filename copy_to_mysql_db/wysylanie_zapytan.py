from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import prettytable

load_dotenv() # to cos pobiera dane z .env w sposob 'cywilizowany' :)

# polaczenie z  .env
engine = create_engine(
  f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}", echo = False)


def run_sql_file(filename):
  with open(filename, 'r', encoding='utf-8') as f:
    # split on single sql instructions
    queries = f.read().split(';')

  with engine.connect() as conn:
    for q in queries:
      clean_q = q.strip()
      if clean_q:
        # print(f"Wykonuję: {clean_q[:50]}...")
        result = conn.execute(text(clean_q))

        # Jeśli to SELECT, wypiszmy wyniki
        if clean_q.lower().startswith('select'):
          table = prettytable.from_db_cursor(result.cursor)
          if table:
            print(table)

    conn.commit()

run_sql_file('zapytania.sql')