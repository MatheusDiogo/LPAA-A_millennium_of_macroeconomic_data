import pandas as pd
import matplotlib.pyplot as plt

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
plt.plot(rebanhos_eng['Year'], rebanhos_eng['Cattle'], label='Gado')
plt.plot(rebanhos_eng['Year'], rebanhos_eng['Sheep'], color='r', label='Ovelha')
plt.plot(rebanhos_eng['Year'], rebanhos_eng['Pigs'], color='k', label='Porco')
plt.title('Comparação')
plt.xlabel('Year')
plt.legend()

plt.suptitle("Number of animals in millions")
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.88, wspace=0.15, hspace=0.35)
