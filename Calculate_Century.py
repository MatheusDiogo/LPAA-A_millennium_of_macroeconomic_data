import pandas as pd

def find_century(year):

    # Calculando seculo caso seja passada uma lista de anos
    if isinstance(year, pd.Series):
        return year.apply(find_century)
        
    # Valores incorretos recebidos retornarão 0
    if (year <= 0):
        return 0
    # Calculando seculo
    elif (year <= 100):
        return 1
    # Se o ano terminar em 0 é preciso apenas pegar seus primeiros números
    elif (year % 100 == 0):
        return year//100
    # Senão é preciso somar mais 1
    else:
        return (year//100)+1
