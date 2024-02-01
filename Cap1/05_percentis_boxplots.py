import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def quartis(serie, *args):
    cabecalho = [str(int(arg*100)) for arg in args]
    percentis = np.quantile(serie, args)
    tuplas = list(zip(cabecalho, percentis))
    df = pd.DataFrame(tuplas, columns=['%', 'Taxa'])
        
    return df


dados = pd.read_csv('Dados/state.csv')

populacao = dados['Population']
taxa_homicidios = dados['Murder.Rate']

qs = quartis(taxa_homicidios, .05, .25, .5, .75, .95)

print(f'Taxa de homicídios\n{qs}\n')

# Gráfico boxplot
figure = plt.figure()
grafico = figure.add_subplot(111)
grafico.boxplot(populacao/1000000)
grafico.set_title('Boxplot População por Estado')
grafico.set_ylabel('População (milhões)')

plt.show()
