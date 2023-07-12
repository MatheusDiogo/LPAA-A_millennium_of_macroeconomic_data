import pandas as pd
import matplotlib.pyplot as plt

#Recebendo dados do google sheets
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQSv10S9cssxOoBF2QGYNukBK-vCgB8fVkhqwtj5n0ASD0OLVBpF15lKakXNUia-90CXokHd47r572c/pub?output=xlsx'

#Recebendo dados e criando DataFrames
agri_eng = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A3. Eng. Agriculture 1270-1870', skiprows = range(0, 10), usecols = 'A, Q:V'))
rebanhos_eng = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A3. Eng. Agriculture 1270-1870', skiprows = range(0, 10), usecols = 'A, Y:AA'))
pecuaria_eng = pd.DataFrame(pd.read_excel(URL, sheet_name = 'A3. Eng. Agriculture 1270-1870', skiprows = range(0, 10), usecols = 'A, AC:AJ'))

#Removendo linhas contendo unidades
agri_eng.drop(index = [0], inplace = True)
agri_eng.reset_index(drop = True, inplace = True)
rebanhos_eng.drop(index = [0], inplace = True)
rebanhos_eng.reset_index(drop = True, inplace = True)
pecuaria_eng.drop(index = [0], inplace = True)
pecuaria_eng.reset_index(drop = True, inplace = True)

#Plotando Gráfico de Série das produções agriculas
plt.plot(agri_eng['Year'], agri_eng['Wheat.1'], label='Trigo')
plt.plot(agri_eng['Year'], agri_eng['Rye.1'], color='r', label='Centeio')
plt.plot(agri_eng['Year'], agri_eng['Barley.1'], color='k', label='Cevada')
plt.plot(agri_eng['Year'], agri_eng['Oats.1'], color='b', label='Aveia')
plt.plot(agri_eng['Year'], agri_eng['Pulses.1'], color='y', label='Pulses')
plt.plot(agri_eng['Year'], agri_eng['Potatoes.1'], color='g', label='Tomate')
plt.xlabel('Year')
plt.ylabel('Production in million bushels)')
plt.title('Produção Agricula Na Inglaterra')
plt.legend()
