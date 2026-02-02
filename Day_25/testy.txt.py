# from sqlalchemy import create_engine
#
# # Format: mysql+pymysql://użytkownik:hasło@IP_MALINKI:PORT/NAZWA_BAZY
# engine = create_engine('mysql+pymysql://admin:mojehaslo@192.168.1.15:3306/pogoda_db')
#
# # I teraz Twoja ulubiona komenda:
# df.to_sql(name='pogoda_tabela', con=engine, if_exists='append', index=False)