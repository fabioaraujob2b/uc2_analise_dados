import pandas as pd
import numpy as np

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_veiculo = df_ocorrencias[['cisp','ano','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo[df_roubo_veiculo['ano'].between(2003,2024)]
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo'])

# Criando o array dos roubo de veiculo
array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])

# Medidas de tendência central
    # Se a média for muito diferente da mediana, distribuição é assimétrica. Não tende a haver um padrão e pode ser que existam outliers (valores discrepantes)
    # Se a média for próxima (25%) a mediana, distribuição é simétrica tende a haver um padrão

# Obtendo a média dos roubo de veiculo
media_roubo_veiculo = np.mean(array_roubo_veiculo)

# Obtendo a mediana dos roubo de veiculo
mediana_roubo_veiculo = np.median(array_roubo_veiculo)

# Obtendo a distância entre a média e a mediana dos roubo de veiculo
distancia_roubo_veiculo = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)

# Obtendo o máximo e o mínimo dos roubo de veiculo
maximo_roubo_veiculo = np.max(array_roubo_veiculo)
minimo_roubo_veiculo = np.min(array_roubo_veiculo)

# Obtendo a amplitude dos roubo de veiculo
amplitude_roubo_veiculo = maximo_roubo_veiculo - minimo_roubo_veiculo

# IQR (Intervalo interquartil)
    # q3 - q1
    # É a amplitude do intervalo dos 50% dos dados centrais
    # Ela ignora os valores extremos. Max e Min que estão fora do IQR
    # Não sofre a interferência dos valores extremos
    # quanto mais próximo de zero, mais homogêneo são os dados
    # quanto mais próximo do q3, mais heterogêneo são os dados

# Obtendo os Quartis dos roubo de veiculo - Método weibull
q1_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
q2_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
q3_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.75, method='weibull')
iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo

# Identificando os outliers superiores e inferiores dos roubo de veiculo
limite_superior_roubo_veiculo = q3_roubo_veiculo + (1.5 * iqr_roubo_veiculo)
limite_inferior_roubo_veiculo = q1_roubo_veiculo - (1.5 * iqr_roubo_veiculo)

# Filtrando o DataFrame roubo de veiculo
df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior_roubo_veiculo]
df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior_roubo_veiculo]

# Medidas de Dispersão
    # É uma medida para observar a dispersão dos dados
    # observa-se em relação a média
    # é a média dos quadrados das diferenças entre cada valor e a média
    # o resultado da variância é elevado ao quadrado
variancia_roubo_veiculo = np.var(array_roubo_veiculo)
distancia_var_roubo_veiculo = variancia_roubo_veiculo / (media_roubo_veiculo ** 2)
devio_padrao_roubo_veiculo = np.std(array_roubo_veiculo)
coeficiente_var_roubo_veiculo = devio_padrao_roubo_veiculo / media_roubo_veiculo

# Exibindo os dados sobre os roubo de veiculo
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS ROUBOS DE VEÍCULOS -----------")
print(f"A média dos roubos de veiculo é {media_roubo_veiculo:.0f}")
print(f"A mediana dos roubos de veiculo é {mediana_roubo_veiculo:.0f}")
print(f"A distância entre a média e a mediana é dos roubos de veiculo é {distancia_roubo_veiculo}")
print(f"O menor valor dos roubo de veiculo é {minimo_roubo_veiculo:.0f}")
print(f"O maior valor dos roubos de veiculo é {maximo_roubo_veiculo:.0f}")
print(f"A amplitude dos valores dos roubos de veiculo é {amplitude_roubo_veiculo:.0f}")
print(f"O valor do q1 - 25% dos roubos de veiculo é {q1_roubo_veiculo:.0f}")
print(f"O valor do q2 - 50% dos roubo de veiculo é {q2_roubo_veiculo:.0f}")
print(f"O valor do q3 - 75% dos roubos de veiculo é {q3_roubo_veiculo:.0f}")
print(f"O valor do iqr = q3 - q1 dos roubos de veiculo é {iqr_roubo_veiculo:.0f}")
print(f"O limite inferior dos roubos de veiculos é {limite_inferior_roubo_veiculo:.0f}")
print(f"O limite superior dos roubos de veiculos é {limite_superior_roubo_veiculo:.0f}")
print(f"O valor da variância dos roubos de veiculo é {variancia_roubo_veiculo:.0f}")
print(f"O coeficiente de variação dos roubos de veiculo é {coeficiente_var_roubo_veiculo:.2f}")
print("O desvio padrão dos roubos de veiculos é", devio_padrao_roubo_veiculo)
print("A distância da variância dos roubos de veiculos é", distancia_var_roubo_veiculo)


print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_veiculo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_veiculo_outliers_superiores.drop(columns='ano').sort_values(by='roubo_veiculo',ascending=False))
