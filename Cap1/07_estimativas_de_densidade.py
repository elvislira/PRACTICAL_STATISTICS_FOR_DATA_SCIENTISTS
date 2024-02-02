import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dados = pd.read_csv('Dados/state.csv')

taxa_homicidios = dados['Murder.Rate']

sns.displot(
    taxa_homicidios,
    kind='kde',
    color='m'
)

plt.hist(
    taxa_homicidios,
    density=True,
    color='c'
)

plt.title('Densidade das taxas de homicídio estaduais')
plt.xlabel('Taxa de homicídios (por 100.000)')
plt.ylabel('Densidade')

plt.show()
