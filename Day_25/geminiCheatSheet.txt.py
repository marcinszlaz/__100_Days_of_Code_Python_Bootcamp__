"""
import pandas as pd
from prettytable import PrettyTable

# 1. Wczytujesz potwora (Pandas)
df = pd.read_csv('weather_data.csv')

# 2. Tworzysz tabelkę
table = PrettyTable()

# 3. Dodajesz nagłówki (kolumny z Pandasa)
table.field_names = df.columns.tolist()

# 4. Dodajesz wszystkie wiersze naraz (df.values to zagnieżdżona lista!)
table.add_rows(df.values.tolist())

# 5. I cyk, gotowe!
print(table)
"""
