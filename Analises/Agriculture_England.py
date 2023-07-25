import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import dataframe_image as dfi
from Calculate_Century import find_century

#Recebendo dados do google sheets
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQSv10S9cssxOoBF2QGYNukBK-vCgB8fVkhqwtj5n0ASD0OLVBpF15lKakXNUia-90CXokHd47r572c/pub?output=xlsx'

#Recebendo dados e criando DataFrames
agri_eng = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A3. Eng. Agriculture 1270-1870', skiprows = range(0, 10), usecols = 'A, Q:V'))
Pasta_Salvar = 'D:\Matheus\Estudos\Python - LPAA\LPAA-A_millennium_of_macroeconomic_data\Graficos_e_Imagens/'

#Removendo linhas contendo unidades
agri_eng.drop(index = [0], inplace = True)
agri_eng.reset_index(drop = True, inplace = True)

#Plotando Gráfico de Série das produções agriculas
plt.figure(figsize = ((20, 10)))
plt.subplot(3, 2, 1)
plt.plot(agri_eng['Year'], agri_eng['Wheat.1'], label='Trigo')
plt.title('Trigo')
plt.xlabel('Year')

plt.subplot(3, 2, 2)
plt.plot(agri_eng['Year'], agri_eng['Rye.1'], color='r', label='Centeio')
plt.title('Centeio')
plt.xlabel('Year')

plt.subplot(3, 2, 3)
plt.plot(agri_eng['Year'], agri_eng['Barley.1'], color='k', label='Cevada')
plt.title('Cevada')
plt.xlabel('Year')

plt.subplot(3, 2, 4)
plt.plot(agri_eng['Year'], agri_eng['Oats.1'], color='b', label='Aveia')
plt.title('Aveia')
plt.xlabel('Year')

plt.subplot(3, 2, 5)
plt.plot(agri_eng['Year'], agri_eng['Pulses.1'], color='y', label='Pulses')
plt.title('Pulses')
plt.xlabel('Year')

plt.subplot(3, 2, 6)
plt.plot(agri_eng['Year'], agri_eng['Potatoes.1'], color='g', label='Tomate')
plt.title('Tomate')
plt.xlabel('Year')

plt.suptitle("Production Agriculture in million bushels", fontsize=20)
plt.tight_layout()
plt.savefig(Pasta_Salvar + 'Production Agriculture in million bushels.png')
plt.close()

#Iniciando análise por séculos
agri_eng['Century'] = find_century(agri_eng['Year'])
dados_Seculo = pd.DataFrame()
dados_Seculo['Wheat'] = agri_eng.groupby(['Century'])['Wheat.1'].sum()
dados_Seculo['Rye'] = agri_eng.groupby(['Century'])['Rye.1'].sum()
dados_Seculo['Barley'] = agri_eng.groupby(['Century'])['Barley.1'].sum()
dados_Seculo['Oats'] = agri_eng.groupby(['Century'])['Oats.1'].sum()
dados_Seculo['Pulses'] = agri_eng.groupby(['Century'])['Pulses.1'].sum()
dados_Seculo['Potatoes'] = agri_eng.groupby(['Century'])['Potatoes.1'].sum()

#Plotando gráfico de barras empilhadas
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.bar(dados_Seculo.index, dados_Seculo['Wheat'], color='orange', label='Trigo')
plt.bar(dados_Seculo.index, dados_Seculo['Rye'], color='purple', label='Centeio', bottom = dados_Seculo['Wheat'])
plt.bar(dados_Seculo.index, dados_Seculo['Barley'], color='gray', label='Cevada', bottom = dados_Seculo['Wheat'] + dados_Seculo['Rye'])
plt.bar(dados_Seculo.index, dados_Seculo['Oats'], color='g', label='Aveia', bottom = dados_Seculo['Wheat'] + dados_Seculo['Rye'] + dados_Seculo['Barley'])
plt.bar(dados_Seculo.index, dados_Seculo['Pulses'], color='pink', label='Pulses', bottom = dados_Seculo['Wheat'] + dados_Seculo['Rye'] + dados_Seculo['Barley'] + dados_Seculo['Oats'])
plt.bar(dados_Seculo.index, dados_Seculo['Potatoes'], label='Tomate', bottom = dados_Seculo['Wheat'] + dados_Seculo['Rye'] + dados_Seculo['Barley'] + dados_Seculo['Oats'] + dados_Seculo['Pulses'])
plt.xlabel('Century')
plt.legend()

# Cálculo da porcentagem de cada produto em relação ao seu século
dados_Seculo_pct = dados_Seculo.div(dados_Seculo.sum(axis=1), axis=0) * 100

# Gráfico único de barras empilhadas com as porcentagens
plt.subplot(1, 2, 2)
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Wheat'], color='orange', label='Trigo')
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Rye'], color='purple', label='Centeio', bottom=dados_Seculo_pct['Wheat'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Barley'], color='gray', label='Cevada', bottom=dados_Seculo_pct['Wheat'] + dados_Seculo_pct['Rye'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Oats'], color='g', label='Aveia', bottom=dados_Seculo_pct['Wheat'] + dados_Seculo_pct['Rye'] + dados_Seculo_pct['Barley'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Pulses'], color='pink', label='Pulses', bottom=dados_Seculo_pct['Wheat'] + dados_Seculo_pct['Rye'] + dados_Seculo_pct['Barley'] + dados_Seculo_pct['Oats'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Potatoes'], label='Tomate', bottom=dados_Seculo_pct['Wheat'] + dados_Seculo_pct['Rye'] + dados_Seculo_pct['Barley'] + dados_Seculo_pct['Oats'] + dados_Seculo_pct['Pulses'])
plt.xlabel('Century')
plt.ylabel('Percentage')
plt.suptitle("Production Agriculture Comparatade")
plt.tight_layout()
plt.savefig(Pasta_Salvar + 'Production Agriculture Comparatade.png')
plt.close()

dfi.export(dados_Seculo_pct.apply(pd.to_numeric, errors='coerce').round().T, Pasta_Salvar + 'Agriculture for Century.png')
plt.close()

# Calculando a matriz de correlação agri_eng e Population of England
agri_eng['Population of England'] = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A2. Pop of Eng & GB 1086-1870', skiprows = range(0, 190), usecols = 'B'))
agri_eng['Potatoes.1'].fillna(0, inplace=True)
agri_eng.dropna(inplace=True)
agri_eng.reset_index(drop=True, inplace=True)
agri_eng = agri_eng.astype(float)

# Seleciona apenas a coluna 'Population of England' e as outras colunas do DataFrame
colunas_selecionadas = ['Population of England'] + list(agri_eng.columns.difference(['Population of England']))

# Calcula a matriz de correlação apenas para as colunas selecionadas
correlation_matrix = agri_eng[colunas_selecionadas].corr()

# Ordena a matriz de correlação com base nos valores da coluna 'Population of England'
correlation_matrix_sorted = correlation_matrix.sort_values(by='Population of England', ascending=False)

# Cria o mapa de calor da correlação ordenada
plt.figure(figsize=(8, 6))
sn.heatmap(correlation_matrix_sorted[['Population of England']], annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, linecolor="k")
plt.title("Correlation Heatmap - Population and Agriculture")
plt.tight_layout()
plt.savefig(Pasta_Salvar + 'Correlation Heatmap - Population and Agriculture.png')
plt.close()