import pandas as pd
import numpy as np
from scipy.stats import median_abs_deviation


dados = pd.read_csv('Dados/state.csv')

populacao = dados['Population']

desvio_padrao = populacao.std()
q75, q25 = np.percentile(populacao, [75, 25])
iqr = q75 - q25
mad = (populacao - populacao.mean()).abs().mean()

print('População')
print(f'\tDesvio padrão = {desvio_padrao:.2f}')
print(f'\tAmplitude Interquartis (IQR): {iqr}')
print(f'\tDesvio absoluto mediano da mediana: {mad:.2f}')
