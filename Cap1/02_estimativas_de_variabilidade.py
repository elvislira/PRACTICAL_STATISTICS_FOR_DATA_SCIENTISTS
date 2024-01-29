from numpy import array
from numpy import average
from numpy import var
from numpy import std
from math import sqrt
from random import randint
from random import seed


seed(100)
amostra = array([float(randint(1, 10)) for i in range(1, 11)])
# Média das amostras
media_amostra = average(amostra)
# Módulo da diferença de cada valor da amostra pela média 
desvios_absoluto = abs(amostra - media_amostra)
# Média dos desvios absolutos
desvio_absoluto_medio = average(desvios_absoluto)
# Quadrado dos desvios
desvios_quadraticos = abs(amostra - media_amostra) ** 2
# Média dos desvios quadráticos
variancia = average(desvios_quadraticos)
# Desvio padrão
desvio_padrao = sqrt(variancia)

print(f'Amostra: {amostra}')
print(f'Média da amostra: {media_amostra:.2f}')
print(f'Desvios absoluto: {desvios_absoluto}')
print(f'Desvio absoluto médio: {desvio_absoluto_medio:.2f}')
print(f'Desvios quadrático: {desvios_quadraticos}')
print(f'Variância: {variancia:.2f} - {var(amostra):.2f}(função var)')
print(f'Desvio padrão: {desvio_padrao:.2f} - {std(amostra):.2f}(função std)')
