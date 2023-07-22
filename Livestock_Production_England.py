import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from Calculate_Century import find_century

#Recebendo dados do google sheets
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQSv10S9cssxOoBF2QGYNukBK-vCgB8fVkhqwtj5n0ASD0OLVBpF15lKakXNUia-90CXokHd47r572c/pub?output=xlsx'

#Recebendo dados e criando DataFrames
pecuaria_eng = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A3. Eng. Agriculture 1270-1870', skiprows = range(0, 10), usecols = 'A, AC:AJ'))

#Removendo linhas contendo unidades
pecuaria_eng.drop(index = [0], inplace = True)
pecuaria_eng.reset_index(drop = True, inplace = True)

#Plotando Gráfico de Série das produções agriculas
plt.figure(figsize = ((19.5, 12)))
plt.subplot(4, 2, 1)
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Milk '])
plt.title('Leite')
plt.xlabel('Year')

plt.subplot(4, 2, 2)
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Beef '], color='r')
plt.title('Carne bovina')
plt.xlabel('Year')

plt.subplot(4, 2, 3)
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Veal '], color='y')
plt.title('Vitela')
plt.xlabel('Year')

plt.subplot(4, 2, 4)
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Mutton '], color='purple')
plt.title('Carne Carneiro')
plt.xlabel('Year')

plt.subplot(4, 2, 5)
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Pork '], color='k')
plt.title('Carne de porco')
plt.xlabel('Year')

plt.subplot(4, 2, 6)
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Wool '], color='b')
plt.title('Lã')
plt.xlabel('Year')

plt.subplot(4, 2, 7)
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Hides'], color='g')
plt.title('Peles')
plt.xlabel('Year')

plt.subplot(4, 2, 8)
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Hay'], color='orange')
plt.title('Feno')
plt.xlabel('Year')

plt.suptitle("Livestock products production in millions")
plt.tight_layout()
plt.savefig('Livestock products production in millions.png')
plt.close()

#Gráfico único
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Beef '], color='r', label='Carne Bovina')
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Milk '], label='Leite')
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Veal '], color='y', label='Vitela')
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Mutton '], color='purple', label='Carne Carneiro')
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Pork '], color='k', label='Carne de Porco')
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Wool '], color='b', label='Lã')
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Hides'], color='g', label='Peles')
plt.plot(pecuaria_eng['Year'], pecuaria_eng['Hay'], color='orange', label='Feno')
plt.legend()
plt.xlabel('Year')
plt.title('Livestock products production in millions')
plt.tight_layout()
plt.savefig('Livestock products production in millions unico.png')
plt.close()

#Recebendo dados por século
pecuaria_eng['Century'] = find_century(pecuaria_eng['Year'])
dados_Seculo = pd.DataFrame()
dados_Seculo['Milk'] = pecuaria_eng.groupby(['Century'])['Milk '].sum()
dados_Seculo['Beef'] = pecuaria_eng.groupby(['Century'])['Beef '].sum()
dados_Seculo['Veal'] = pecuaria_eng.groupby(['Century'])['Veal '].sum()
dados_Seculo['Mutton'] = pecuaria_eng.groupby(['Century'])['Mutton '].sum()
dados_Seculo['Pork'] = pecuaria_eng.groupby(['Century'])['Pork '].sum()
dados_Seculo['Wool'] = pecuaria_eng.groupby(['Century'])['Wool '].sum()
dados_Seculo['Hides'] = pecuaria_eng.groupby(['Century'])['Hides'].sum()
dados_Seculo['Hay'] = pecuaria_eng.groupby(['Century'])['Hay'].sum()
dados_Seculo

#Plotando gráfico de barras empilhadas
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.bar(dados_Seculo.index, dados_Seculo['Milk'], color='orange', label='Milk')
plt.bar(dados_Seculo.index, dados_Seculo['Beef'], color='purple', label='Beef', bottom = dados_Seculo['Milk'])
plt.bar(dados_Seculo.index, dados_Seculo['Veal'], color='gray', label='Veal', bottom = dados_Seculo['Milk'] + dados_Seculo['Beef'])
plt.bar(dados_Seculo.index, dados_Seculo['Mutton'], color='g', label='Mutton', bottom = dados_Seculo['Milk'] + dados_Seculo['Beef'] + dados_Seculo['Veal'])
plt.bar(dados_Seculo.index, dados_Seculo['Pork'], color='pink', label='Pork', bottom = dados_Seculo['Milk'] + dados_Seculo['Beef'] + dados_Seculo['Veal']  + dados_Seculo['Mutton'])
plt.bar(dados_Seculo.index, dados_Seculo['Wool'], color='b', label='Wool', bottom = dados_Seculo['Milk'] + dados_Seculo['Beef'] + dados_Seculo['Veal'] + dados_Seculo['Mutton'] + dados_Seculo['Pork'])
plt.bar(dados_Seculo.index, dados_Seculo['Hides'], color='y', label='Hides', bottom = dados_Seculo['Milk'] + dados_Seculo['Beef'] + dados_Seculo['Veal'] + dados_Seculo['Mutton'] + dados_Seculo['Pork'] + dados_Seculo['Wool'])
plt.bar(dados_Seculo.index, dados_Seculo['Hay'], color='r', label='Hay', bottom = dados_Seculo['Milk'] + dados_Seculo['Beef'] + dados_Seculo['Veal'] + dados_Seculo['Mutton'] + dados_Seculo['Pork'] + dados_Seculo['Wool'] + dados_Seculo['Hides'])
plt.xlabel('Century')
plt.legend()

# Cálculo da porcentagem de cada produto em relação ao seu século
dados_Seculo_pct = dados_Seculo.div(dados_Seculo.sum(axis=1), axis=0) * 100

# Gráfico de barras empilhadas com as porcentagens
plt.subplot(1, 2, 2)
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Milk'], color='orange', label='Milk')
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Beef'], color='purple', label='Beef', bottom = dados_Seculo_pct['Milk'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Veal'], color='gray', label='Veal', bottom = dados_Seculo_pct['Milk'] + dados_Seculo_pct['Beef'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Mutton'], color='g', label='Mutton', bottom = dados_Seculo_pct['Milk'] + dados_Seculo_pct['Beef'] + dados_Seculo_pct['Veal'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Pork'], color='pink', label='Pork', bottom = dados_Seculo_pct['Milk'] + dados_Seculo_pct['Beef'] + dados_Seculo_pct['Veal']  + dados_Seculo_pct['Mutton'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Wool'], color='b', label='Wool', bottom = dados_Seculo_pct['Milk'] + dados_Seculo_pct['Beef'] + dados_Seculo_pct['Veal'] + dados_Seculo_pct['Mutton'] + dados_Seculo_pct['Pork'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Hides'], color='y', label='Hides', bottom = dados_Seculo_pct['Milk'] + dados_Seculo_pct['Beef'] + dados_Seculo_pct['Veal'] + dados_Seculo_pct['Mutton'] + dados_Seculo_pct['Pork'] + dados_Seculo_pct['Wool'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Hay'], color='r', label='Hay', bottom = dados_Seculo_pct['Milk'] + dados_Seculo_pct['Beef'] + dados_Seculo_pct['Veal'] + dados_Seculo_pct['Mutton'] + dados_Seculo_pct['Pork'] + dados_Seculo_pct['Wool'] + dados_Seculo_pct['Hides'])

plt.xlabel('Century')
plt.ylabel('Percentage')
plt.suptitle("Livestock products production comparatade")
plt.tight_layout()
plt.savefig('Livestock products production comparatade.png')

# Calculando a matriz de correlação agri_eng e Population of England
pecuaria_eng['Population of England'] = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A2. Pop of Eng & GB 1086-1870', skiprows = range(0, 190), usecols = 'B'))
pecuaria_eng.dropna(inplace=True)
pecuaria_eng.reset_index(drop=True, inplace=True)
pecuaria_eng = pecuaria_eng.astype(float)

# Seleciona apenas a coluna 'Population of England' e as outras colunas do DataFrame
colunas_selecionadas = ['Population of England'] + list(pecuaria_eng.columns.difference(['Population of England']))

# Calcula a matriz de correlação apenas para as colunas selecionadas
correlation_matrix = pecuaria_eng[colunas_selecionadas].corr()

# Ordena a matriz de correlação com base nos valores da coluna 'Population of England'
correlation_matrix_sorted = correlation_matrix.sort_values(by='Population of England', ascending=False)

# Cria o mapa de calor da correlação ordenada
plt.figure(figsize=(8, 6))
sn.heatmap(correlation_matrix_sorted[['Population of England']], annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, linecolor="k")
plt.title("Correlation Heatmap - Population and Livestock")
plt.tight_layout()
plt.savefig('Correlation Heatmap - Population and Livestock.png')
plt.close()