from random import seed
from random import randint
import numpy as np


seed(100)
amostra = np.array([randint(1, 10) for i in range(9)])
# amostra = [13, 25, 69, 72, 33, 41, 28, 17, 65]

q25, q50, q75 = np.percentile(amostra, [25, 50, 75])

print(f'Amostra: {amostra}')
print(f'Amostra ordenada: {sorted(amostra)}')
print(f'Q25: {q25}')
print(f'Q50: {q50}')
print(f'Q75: {q75}')
