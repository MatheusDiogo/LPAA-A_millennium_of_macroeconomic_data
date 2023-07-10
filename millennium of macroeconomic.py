import pandas as pd
import matplotlib.pyplot as plt

#Recebendo dados do google sheets
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQSv10S9cssxOoBF2QGYNukBK-vCgB8fVkhqwtj5n0ASD0OLVBpF15lKakXNUia-90CXokHd47r572c/pub?output=xlsx'

df = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A2. Pop of Eng & GB 1086-1870', skiprows = range(0, 7)))

#Removendo dados Nan do banco de dados
df['Year'].dropna(inplace = True)
df['Population of England, millions'].fillna('0', inplace = True)
df['Population of Great Britain, millions'].fillna('0', inplace = True)
df['Year'] = df['Year'].astype(float)
df['Population of England, millions'] = df['Population of England, millions'].astype(float)
df['Population of Great Britain, millions'] = df['Population of Great Britain, millions'].astype(float)
df.reset_index(drop = True, inplace= True)
