import pandas as pd
import matplotlib.pyplot as plt


dados = pd.read_csv('Dados/state.csv')

populacao = dados['Population']

frequencia = pd.value_counts(
    pd.cut(
        x=populacao,
        bins=10, 
        include_lowest=True,
        right=False
    ),
    sort=False
)

tabela_frequencias = pd.DataFrame(frequencia)

print(tabela_frequencias['count'])

plt.hist(populacao/1000000, 10, color='g')

plt.title('Histograma de Populações Estaduais')
plt.axis(ymin=0, ymax=25)
plt.xlabel('População (milhões)')
plt.grid(axis='y')

plt.show()
