# Pandas para ler os dados do arquivo states.csv
import pandas as pd
# Libs para cálculo das estimativas de localização
from statistics import mean
from statistics import median
from scipy.stats import trim_mean
from numpy import average
#Libs para fazer o gráfico
from pylab import barh
from pylab import show
from pylab import xlabel
from pylab import ylabel
from pylab import grid
from pylab import title
from pylab import axvline
from pylab import text


dados = pd.read_csv('Dados/state.csv')

populacao = round((dados['Population'] / 1000000), 2)

# Soma de todos os valores divida pela quantidade de valores
media_populacao = round(mean(populacao), 2)

# Valor central dos dados ou a média dos dois valores centrais, 
# caso a quantidade de valores seja ímpar 
mediana_populacao = round(median(populacao), 2)

# Média dos valores após a exclusão de 10% dos valores extremos
# (manores e maiores valores)
media_aparada_populacao = round(trim_mean(populacao, 0.1), 2)

# Média ponderada das taxas de homicídio, onde a população de cada 
# cidade é considerada no cálculo (pesa no resultado)
taxa_media_homicidios_pais = round(average(dados['Murder.Rate'], weights=populacao), 2)

# Gráfico de barras com a população de todos os estados
barh(
    dados['State'],
    populacao,
    align='center',
    color=['c', 'b']
)

title('USA - População por Estados')
xlabel('População (milhões habitantes)')
ylabel('Estados')

text(
    max(populacao)/2,
    25,
    f'\nTaxa média de homicídios do país: {taxa_media_homicidios_pais}\n'
)

axvline(x=media_populacao, color='g')
text(
    media_populacao, 
    2, 
    f'Média({media_populacao})', 
    rotation='horizontal',
    color='g'
)

axvline(x=mediana_populacao, color='k')
text(
    mediana_populacao, 
    -0, 
    f'Mediana({mediana_populacao})', 
    rotation='horizontal', 
    color='k'
)

axvline(x=media_aparada_populacao, color='r')
text(
    media_aparada_populacao, 
    -2, 
    f'Média aparada({media_aparada_populacao})', 
    rotation='horizontal', 
    color='r'
)

grid(axis='x')

show()
