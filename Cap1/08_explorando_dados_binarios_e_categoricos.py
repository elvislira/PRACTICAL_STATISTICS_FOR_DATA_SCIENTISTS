import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def calcula_porcentagens(dados):
    total_atrasos = dados.sum(axis=1)
    cia = dados['Carrier'] / total_atrasos * 100
    atc = dados['ATC'] / total_atrasos * 100
    weather = dados['Weather'] / total_atrasos * 100
    security = dados['Security'] / total_atrasos * 100
    inbound = dados['Inbound'] / total_atrasos * 100
    
    return [
        round(cia, 2)[0],
        round(atc, 2)[0],
        round(weather, 2)[0],
        round(security, 2)[0],
        round(inbound, 2)[0]
    ]
    
def exibe_porcentagens(porcentagens):
    cabecalho = '{:<12}{:<12}{:<12}{:<12}{:<12}'.format('Cia', 'CTA', 'Clima', 'Segurança', 'Entrada')
    linhas = f'{str(porcentagens[0]):12s}{str(porcentagens[1]):12s}' \
        f'{str(porcentagens[2]):12s}{str(porcentagens[3]):12s}' \
        f'{str(porcentagens[4]):12s}'
        
    print('Porcentagem de atrasos por causador no' \
        ' aeroporto de Dallas-Fort Worth')
    print(f'{cabecalho}\n{linhas}')
    
def exibe_grafico(porcentagens):
    x = ['Cia', 'ATC', 'Clima', 'Segurança', 'Entrada']
    cores = ['Red', 'Orange', 'Blue', 'Purple', 'Green']

    grafico = plt.bar(
        x,
        porcentagens,
        color=cores
    )

    i = 0

    for p in grafico:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        plt.text(
            x + width/2,
            y + height * 1.01,
            str(porcentagens[i]) + '%',
            ha='center',
            weight='bold',
            color=cores[i]
        )
        
        i += 1

    plt.title('Porcentagem de atrasos por causador no\n' \
            'aeroporto de Dallas-Fort Worth')
    plt.ylabel('Porcentagem')
    plt.xlabel('Causa')
    plt.grid(axis='y')

    plt.show()
 
dados = pd.read_csv('Dados/dfw_airline.csv')

porcentagens = calcula_porcentagens(dados)

exibe_porcentagens(porcentagens)

exibe_grafico(porcentagens)
