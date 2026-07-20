import pandas as pd
import numpy as np
import json

# Command for uv installing
# curl -LsSf https://astral.sh/uv/install.sh | sh  for linux/mac
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" for windows powershell

# df = pd.read_csv('./orders.csv')
# print(df)

"""
df = pd.read_csv('data.csv')      # Load from CSV
df = pd.read_excel('data.xlsx')   # Load from Excel
df = pd.DataFrame(data_dict)      # Load from dictionary
"""

# x = np.linspace(start=0, stop=10, num=100)
# print(x)
#
# _ = list(range(1900,1920,5))
# print(_)
# np.array(ndmin=1900, ndmax=1920, like=5)
z = np.arange(1900, 2021, step=5)
print(z)

x = pd.to_datetime('2020')
print(x)