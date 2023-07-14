def find_century(year):
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
