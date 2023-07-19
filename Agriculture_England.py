import pandas as pd
import matplotlib.pyplot as plt
from Calculate_Century import find_century

#Recebendo dados do google sheets
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQSv10S9cssxOoBF2QGYNukBK-vCgB8fVkhqwtj5n0ASD0OLVBpF15lKakXNUia-90CXokHd47r572c/pub?output=xlsx'

#Recebendo dados e criando DataFrames
agri_eng = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A3. Eng. Agriculture 1270-1870', skiprows = range(0, 10), usecols = 'A, Q:V'))

#Removendo linhas contendo unidades
agri_eng.drop(index = [0], inplace = True)
agri_eng.reset_index(drop = True, inplace = True)

#Plotando Gráfico de Série das produções agriculas
plt.figure(figsize = ((19.5, 12)))
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

plt.suptitle("Production Agriculture in million bushels", fontsize=30)
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.97, wspace=0.15, hspace=0.4)
plt.savefig('Production Agriculture in million bushels.png')

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
plt.subplot(1, 2, 1)
plt.bar(dados_Seculo.index, dados_Seculo['Wheat'], color='orange', label='Wheat')
plt.bar(dados_Seculo.index, dados_Seculo['Rye'], color='purple', label='Rye', bottom = dados_Seculo['Wheat'])
plt.bar(dados_Seculo.index, dados_Seculo['Barley'], color='gray', label='Barley', bottom = dados_Seculo['Wheat'] + dados_Seculo['Rye'])
plt.bar(dados_Seculo.index, dados_Seculo['Oats'], color='g', label='Oats', bottom = dados_Seculo['Wheat'] + dados_Seculo['Rye'] + dados_Seculo['Barley'])
plt.bar(dados_Seculo.index, dados_Seculo['Pulses'], color='pink', label='Pulses', bottom = dados_Seculo['Wheat'] + dados_Seculo['Rye'] + dados_Seculo['Barley'] + dados_Seculo['Oats'])
plt.bar(dados_Seculo.index, dados_Seculo['Potatoes'], label='Potatoes', bottom = dados_Seculo['Wheat'] + dados_Seculo['Rye'] + dados_Seculo['Barley'] + dados_Seculo['Oats'] + dados_Seculo['Pulses'])
plt.xlabel('Century')
plt.legend(fontsize=25)

# Cálculo da porcentagem de cada produto em relação ao seu século
dados_Seculo_pct = dados_Seculo.div(dados_Seculo.sum(axis=1), axis=0) * 100

# Gráfico único de barras empilhadas com as porcentagens
plt.subplot(1, 2, 2)
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Wheat'], color='orange', label='Wheat')
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Rye'], color='purple', label='Rye', bottom=dados_Seculo_pct['Wheat'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Barley'], color='gray', label='Barley', bottom=dados_Seculo_pct['Wheat'] + dados_Seculo_pct['Rye'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Oats'], color='g', label='Oats', bottom=dados_Seculo_pct['Wheat'] + dados_Seculo_pct['Rye'] + dados_Seculo_pct['Barley'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Pulses'], color='pink', label='Pulses', bottom=dados_Seculo_pct['Wheat'] + dados_Seculo_pct['Rye'] + dados_Seculo_pct['Barley'] + dados_Seculo_pct['Oats'])
plt.bar(dados_Seculo_pct.index, dados_Seculo_pct['Potatoes'], label='Potatoes', bottom=dados_Seculo_pct['Wheat'] + dados_Seculo_pct['Rye'] + dados_Seculo_pct['Barley'] + dados_Seculo_pct['Oats'] + dados_Seculo_pct['Pulses'])
plt.xlabel('Century')
plt.ylabel('Percentage')
plt.suptitle("Production Agriculture Comparatade", fontsize=30)
plt.savefig('Production Agriculture Comparatade.png')