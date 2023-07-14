import pandas as pd
import matplotlib.pyplot as plt

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
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.92, wspace=0.15, hspace=0.4)

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
plt.title('Livestock products production in millions')
plt.xlabel('Year')
