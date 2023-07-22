import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from Calculate_Century import find_century

#Recebendo dados do google sheets
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQSv10S9cssxOoBF2QGYNukBK-vCgB8fVkhqwtj5n0ASD0OLVBpF15lKakXNUia-90CXokHd47r572c/pub?output=xlsx'

#Recebendo dados e criando DataFrames
rebanhos_eng = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A3. Eng. Agriculture 1270-1870', skiprows = range(0, 10), usecols = 'A, Y:AA'))

#Removendo linhas contendo unidades
rebanhos_eng.drop(index = [0], inplace = True)
rebanhos_eng.reset_index(drop = True, inplace = True)

#Plotando Gráfico de Série das produções agriculas
plt.figure(figsize = ((12, 6)))
plt.subplot(2, 2, 1)
plt.plot(rebanhos_eng['Year'], rebanhos_eng['Cattle'], label='Gado')
plt.title('Gado')
plt.xlabel('Year')

plt.subplot(2, 2, 2)
plt.plot(rebanhos_eng['Year'], rebanhos_eng['Sheep'], color='r', label='Ovelha')
plt.title('Ovelha')
plt.xlabel('Year')

plt.subplot(2, 2, 3)
plt.plot(rebanhos_eng['Year'], rebanhos_eng['Pigs'], color='k', label='Porco')
plt.title('Porco')
plt.xlabel('Year')

#Gráfico único
plt.subplot(2, 2, 4)
plt.plot(rebanhos_eng['Year'], rebanhos_eng['Cattle'], label='Gado')
plt.plot(rebanhos_eng['Year'], rebanhos_eng['Sheep'], color='r', label='Ovelha')
plt.plot(rebanhos_eng['Year'], rebanhos_eng['Pigs'], color='k', label='Porco')
plt.title('Comparação')
plt.xlabel('Year')
plt.legend()

plt.suptitle("Number of animals in millions")
plt.tight_layout()
plt.savefig('Number of animals in millions.png')
plt.close()

#Análise gráfica por século
rebanhos_eng['Century'] = find_century(rebanhos_eng['Year'])
dados_Seculo = pd.DataFrame()
dados_Seculo['Cattle'] = rebanhos_eng.groupby(['Century'])['Cattle'].sum()
dados_Seculo['Sheep'] = rebanhos_eng.groupby(['Century'])['Sheep'].sum()
dados_Seculo['Pigs'] = rebanhos_eng.groupby(['Century'])['Pigs'].sum()

#Plotando gráfico de barras empilhadas
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.bar(dados_Seculo.index, dados_Seculo['Cattle'], color='orange', label='Gado')
plt.bar(dados_Seculo.index, dados_Seculo['Sheep'], label='Ovelha', bottom = dados_Seculo['Cattle'])
plt.bar(dados_Seculo.index, dados_Seculo['Pigs'], color='g', label='Porco', bottom = dados_Seculo['Cattle'] + dados_Seculo['Sheep'])
plt.xlabel('Century')
plt.legend()

# Cálculo da porcentagem de cada produto em relação ao seu século
dados_Seculo_pct = dados_Seculo.div(dados_Seculo.sum(axis=1), axis=0) * 100

# Gráfico único de barras empilhadas com as porcentagens
plt.subplot(1, 2, 2)
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Cattle'], color='orange', label='Gado')
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Sheep'], label='Ovelha', bottom = dados_Seculo_pct['Cattle'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Pigs'], color='g', label='Porco', bottom = dados_Seculo_pct['Cattle'] + dados_Seculo_pct['Sheep'])

plt.xlabel('Century')
plt.ylabel('Percentage')
plt.suptitle("Number of animals Comparatade")
plt.tight_layout()
plt.savefig('Number of animals Comparatade.png')
plt.close()

# Calculando a matriz de correlação agri_eng e Population of England
rebanhos_eng['Population of England'] = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A2. Pop of Eng & GB 1086-1870', skiprows = range(0, 190), usecols = 'B'))
rebanhos_eng.dropna(inplace=True)
rebanhos_eng.reset_index(drop=True, inplace=True)
rebanhos_eng = rebanhos_eng.astype(float)

# Seleciona apenas a coluna 'Population of England' e as outras colunas do DataFrame
colunas_selecionadas = ['Population of England'] + list(rebanhos_eng.columns.difference(['Population of England']))

# Calcula a matriz de correlação apenas para as colunas selecionadas
correlation_matrix = rebanhos_eng[colunas_selecionadas].corr()

# Ordena a matriz de correlação com base nos valores da coluna 'Population of England'
correlation_matrix_sorted = correlation_matrix.sort_values(by='Population of England', ascending=False)

# Cria o mapa de calor da correlação ordenada
plt.figure(figsize=(8, 6))
sn.heatmap(correlation_matrix_sorted[['Population of England']], annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, linecolor="k")
plt.title("Correlation Heatmap - Population and Animals")
plt.tight_layout()
plt.savefig('Correlation Heatmap - Population and Animals.png')
plt.close()