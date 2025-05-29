import pandas as pd
import numpy as np

# Importando a base de dados de ocorrências 
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame de ocorrências
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_cargas = df_ocorrencias[['cisp', 'roubo_carga', 'ano']]
df_cargas = df_cargas[df_cargas['ano'].between(2003, 2024)]
df_cargas = df_cargas.groupby(['cisp']).sum(['roubo_carga']).reset_index()
# Exibindo a base de dados de ocorrências
print(df_cargas)
# Obtendo informações sobre ocorrências de roubo de carga por município


array_roubos = df_cargas['roubo_carga']

media_roubos = np.mean(array_roubos)
mediana_roubos = np.median(array_roubos)
distancia_roubos = abs((media_roubos - mediana_roubos) / mediana_roubos)
maior_qtd_roubos = np.max(array_roubos)
menor_qtd_roubos = np.min(array_roubos)
amplitute_roubos = maior_qtd_roubos - menor_qtd_roubos

q1_roubos = np.quantile(array_roubos, 0.25, method='weibull')
q2_roubos = np.quantile(array_roubos, 0.50, method='weibull')
q3_roubos = np.quantile(array_roubos, 0.75, method='weibull')
iqr_roubos = q3_roubos - q1_roubos

limite_superior_roubos = q3_roubos + (1.5 * iqr_roubos)
limite_inferior_roubos = q1_roubos - (1.5 * iqr_roubos)

df_roubos_outliers_superiores = df_cargas[df_cargas['roubo_carga'] > limite_superior_roubos]
df_roubos_outliers_inferiores = df_cargas[df_cargas['roubo_carga'] < limite_inferior_roubos]


print(f"A média das ocorrências de roubo de carga por município é {media_roubos:.2f}.")
print(f"A mediana das ocorrências de roubo de carga por município é {mediana_roubos:.2f}.")
print(f"A distância entre a média e a mediana das ocorrências de roubo de carga por município é {distancia_roubos:.2f}%.")
print(f"A maior quantidade de ocorrências de roubo de carga por município é {maior_qtd_roubos}.")
print(f"A menor quantidade de ocorrências de roubo de carga por município é {menor_qtd_roubos}.")
print(f"A amplitute das ocorrências de roubo de carga por município é {amplitute_roubos}.")
print(f"Q1 das ocorrências de roubo de carga por município é {q1_roubos:.2f}.")
print(f"Q2 das ocorrências de roubo de carga por município é {q2_roubos:.2f}.")
print(f"Q3 das ocorrências de roubo de carga por município é {q3_roubos:.2f}.")
print(f"O IQR das ocorrências de roubo de carga por município é {iqr_roubos:.2f}.")
print(f"O limite superior das ocorrências de roubo de carga por município é {limite_superior_roubos:.2f}.")
print(f"O limite inferior das ocorrências de roubo de carga por município é {limite_inferior_roubos:.2f}.")

if len(df_roubos_outliers_inferiores) == 0:
    print('Não existem outliers inferiores.')
else:
    print(f"Existem {df_roubos_outliers_inferiores} outliers inferiores.")

if len(df_roubos_outliers_superiores) == 0:
    print('Não existem outliers superiores.')
else:
    print(df_roubos_outliers_superiores.drop(columns='ano').sort_values('roubo_carga', ascending=False))

