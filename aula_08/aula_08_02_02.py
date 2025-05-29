import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_recuperacao_veiculo = df_ocorrencias[['aisp','ano','recuperacao_veiculos']]
df_recuperacao_veiculo = df_recuperacao_veiculo[df_recuperacao_veiculo['ano'].between(2003,2024)]
df_recuperacao_veiculo = df_recuperacao_veiculo.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index()

# Criando o array das recuperações de veiculos
array_recuperacao_veiculo = np.array(df_recuperacao_veiculo["recuperacao_veiculos"])

# Medidas de Tendência Central
    # Se a média for muito diferente da mediana, distribuição é assimétrica. Não tende a haver um padrão e pode ser que existam outliers (valores discrepantes)
    # Se a média for próxima (25%) a mediana, distribuição é simétrica tende a haver um padrão

# Obtendo a média das recuperações de veiculos
media_recuperacao_veiculo = np.mean(array_recuperacao_veiculo)

# Obtendo a mediana das recuperações de veiculos
mediana_recuperacao_veiculo = np.median(array_recuperacao_veiculo)

# Obtendo a distância entre a média e a mediana das recuperações de veiculos
distancia_recuperacao_veiculo = abs((media_recuperacao_veiculo - mediana_recuperacao_veiculo) / mediana_recuperacao_veiculo)

# Obtendo o máximo e o mínimo das recuperações de veiculos
maximo_recuperacao_veiculo = np.max(array_recuperacao_veiculo)
minimo_recuperacao_veiculo = np.min(array_recuperacao_veiculo)

# Obtendo a amplitude das recuperações de veiculos
amplitude_recuperacao_veiculo = maximo_recuperacao_veiculo - minimo_recuperacao_veiculo

# IQR (Intervalo interquartil)
    # q3 - q1
    # É a amplitude do intervalo dos 50% dos dados centrais
    # Ela ignora os valores extremos. Max e Min que estão fora do IQR
    # Não sofre a interferência dos valores extremos
    # quanto mais próximo de zero, mais homogêneo são os dados
    # quanto mais próximo do q3, mais heterogêneo são os dados

# Obtendo os Quartis das recuperações de veiculos - Método weibull
q1_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.25, method='weibull')
q2_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.50, method='weibull')
q3_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.75, method='weibull')
iqr_recuperacao_veiculo = q3_recuperacao_veiculo - q1_recuperacao_veiculo

# Identificando os outliers superiores e inferiores das recuperações de veiculos
limite_superior_recuperacao_veiculo = q3_recuperacao_veiculo + (1.5 * iqr_recuperacao_veiculo)
limite_inferior_recuperacao_veiculo = q1_recuperacao_veiculo - (1.5 * iqr_recuperacao_veiculo)

# Filtrando o DataFrame das recuperações de veiculos
df_recuperacao_veiculo_outliers_superiores = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] > limite_superior_recuperacao_veiculo]
df_recuperacao_veiculo_outliers_inferiores = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] < limite_inferior_recuperacao_veiculo]

# Medidas de Dispersão
    # É uma medida para observar a dispersão dos dados
    # observa-se em relação a média
    # é a média dos quadrados das diferenças entre cada valor e a média
    # o resultado da variância é elevado ao quadrado
variancia_recuperacao_veiculo = np.var(array_recuperacao_veiculo)
distancia_var_recuperacao_veiculo = variancia_recuperacao_veiculo / (media_recuperacao_veiculo ** 2)
devio_padrao_recuperacao_veiculo = np.std(array_recuperacao_veiculo)
coeficiente_var_recuperacao_veiculo = devio_padrao_recuperacao_veiculo / media_recuperacao_veiculo


# Exibindo os dados sobre os roubo de veiculo
print("\n--------- OBTENDO INFORMAÇÕES SOBRE AS RECUPERAÇÕES DE VEÍCULOS -----------")
print(f"A média das recuperações de veiculos é {media_recuperacao_veiculo:.0f}")
print(f"A mediana das recuperações de veiculos é {mediana_recuperacao_veiculo:.0f}")
print(f"A distância entre a média e a mediana é das recuperações de veiculos é {distancia_recuperacao_veiculo}")
print(f"O menor valor das recuperações de veiculos é {minimo_recuperacao_veiculo:.0f}")
print(f"O maior valor das recuperações de veiculos é {maximo_recuperacao_veiculo:.0f}")
print(f"A amplitude dos valores das recuperações de veiculos é {amplitude_recuperacao_veiculo:.0f}")
print(f"O valor do q1 - 25% das recuperações de veiculos é {q1_recuperacao_veiculo:.0f}")
print(f"O valor do q2 - 50% das recuperações de veiculos é {q2_recuperacao_veiculo:.0f}")
print(f"O valor do q3 - 75% das recuperações de veiculos é {q3_recuperacao_veiculo:.0f}")
print(f"O valor do iqr = q3 - q1 das recuperações de veiculos é {iqr_recuperacao_veiculo:.0f}")
print(f"O limite inferior das recuperações de veiculos é {limite_inferior_recuperacao_veiculo:.0f}")
print(f"O limite superior das recuperações de veiculos é {limite_superior_recuperacao_veiculo:.0f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_recuperacao_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_recuperacao_veiculo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_recuperacao_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_recuperacao_veiculo_outliers_superiores.drop(columns='ano').sort_values(by='recuperacao_veiculos',ascending=False))

# Visualizando os dados sobre os roubos de veiculo
print('\n- Visualizando os dados sobre as Recuperações de Veículos -')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre as Recuperações de Veículos de 2003 até 2024',fontsize=16)

# posição 01: Gráfico das Recuperações de Veículos
plt.subplot(2,2,1)
plt.title('Boxplot das Recuperações de Veículos')
plt.boxplot(array_recuperacao_veiculo,vert=False,showmeans=True)

# Posição 02: Histograma das Recuperações de Veículos
plt.subplot(2,2,2)
plt.title('Histograma das Recuperações de Veículos')
plt.hist(array_recuperacao_veiculo,bins=100,edgecolor='black')    

# Posição 03: Gráfico dos Outliers das Recuperações de Veículos
df_recuperacao_veiculo_outliers_superiores_order = df_recuperacao_veiculo_outliers_superiores.sort_values(by='recuperacao_veiculos',ascending=True)
plt.subplot(2,2,3)
plt.title('Gráfico das Recuperações de Veículos')
plt.barh(df_recuperacao_veiculo_outliers_superiores_order['aisp'].astype(str),df_recuperacao_veiculo_outliers_superiores_order['recuperacao_veiculos'])

# Posição 04: Medidas Descritivas das Recuperações de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas das Recuperações de Veículos',fontsize=12)
plt.axis('off')
plt.text(0.1,0.9,f'Média das Recuperações de Veículos: {media_recuperacao_veiculo:.0f}',fontsize=11)
plt.text(0.1,0.8,f'Mediana das Recuperações de Veículos: {mediana_recuperacao_veiculo:.0f}',fontsize=11)
plt.text(0.1,0.7,f'Distância entre a Média e a Mediana das Recuperações de Veículos: {distancia_recuperacao_veiculo}',fontsize=11)
plt.text(0.1,0.6,f'Menor Valor das Recuperações de Veículos: {minimo_recuperacao_veiculo:.0f}',fontsize=11)
plt.text(0.1,0.5,f'Maior Valor das Recuperações de Veículos: {maximo_recuperacao_veiculo:.0f}',fontsize=11)
plt.text(0.1,0.4,f'O coeficiente de variação das Recuperações de veiculo é {coeficiente_var_recuperacao_veiculo:.2f}',fontsize=11)
plt.text(0.1,0.3,f'A distância da variância das Recuperações de veiculos é, {distancia_var_recuperacao_veiculo:.2f}',fontsize=11)

plt.show()