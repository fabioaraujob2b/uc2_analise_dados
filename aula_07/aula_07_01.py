import pandas as pd
import numpy as np

# Importando a base de dados de ocorrências 
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame de ocorrências
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')

# Exibindo a base de dados de ocorrências
df_hom_doloso = df_ocorrencias[['ano', 'hom_doloso']]
df_hom_doloso = df_hom_doloso[df_hom_doloso['ano'].between(2003, 2024)]
df_hom_doloso = df_hom_doloso.groupby(['ano']).sum(['hom_doloso']).reset_index()

print(df_hom_doloso)

# Obtendo informações sobre homicídeos dolosos por ano

media_hom = np.mean(df_hom_doloso['hom_doloso'])
mediana_hom = np.median(df_hom_doloso['hom_doloso'])
distancia_hom = abs((media_hom - mediana_hom) / mediana_hom) * 100
maior_qtd_hom = np.max(df_hom_doloso['hom_doloso'])
menor_qtd_hom = np.min(df_hom_doloso['hom_doloso'])

ano_maior = df_hom_doloso[df_hom_doloso['hom_doloso'] == maior_qtd_hom]['ano'].values[0]
ano_menor = df_hom_doloso[df_hom_doloso['hom_doloso'] == menor_qtd_hom]['ano'].values[0]

amplitute_hom = maior_qtd_hom - menor_qtd_hom

q1_hom = np.quantile(df_hom_doloso['hom_doloso'], 0.25)
q2_hom = np.quantile(df_hom_doloso['hom_doloso'], 0.50)
q3_hom = np.quantile(df_hom_doloso['hom_doloso'], 0.75)
iqr_hom = q3_hom - q1_hom

limite_superior_hom = q3_hom + (1.5 * iqr_hom)
limite_inferior_hom = q1_hom - (1.5 * iqr_hom)

df_fare_outliers_inferiores = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior_hom]
df_fare_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior_hom]

print('\n-- OBTENDO INFORMAÇÕES SOBRE HOMICÍDEOS DOLOSOS POR ANO --\n')
print(f'A média de homicídeos dolosos por ano é: {media_hom:.2f}')
print(f'A mediana de homicídeos dolosos por ano é: {mediana_hom:.3f}')
print(f'A distância entre a média e a mediana de homicídeos dolosos por ano é: {distancia_hom:.2f}%')
print(f'O maior número de homicídeos dolosos por ano é: {maior_qtd_hom} que foi no ano de {ano_maior}')
print(f'O menor número de homicídeos dolosos por ano é: {menor_qtd_hom} que foi no ano de {ano_menor}')
print(f'A amplitude dos homicídeos dolosos por ano é: {amplitute_hom}')
print(f'Q1 dos homicídeos dolosos por ano é: {q1_hom:.2f}')
print(f'Q2 dos homicídeos dolosos por ano é: {q2_hom:.2f}')
print(f'Q3 dos homicídeos dolosos por ano é: {q3_hom:.2f}')
print(f'IQR dos homicídeos dolosos por ano é: {iqr_hom:.2f}')
print(f'Limite Superior dos homicídeos dolosos por ano é: {limite_superior_hom:.2f}')
print(f'Limite Inferior dos homicídeos dolosos por ano é: {limite_inferior_hom:.2f}')
if df_fare_outliers_inferiores.empty == False:
    print(f'Existem {len(df_fare_outliers_inferiores)} outliers inferiores')
    print(f'Existem {len(df_fare_outliers_superiores)} outliers superiores')
else:
    print(f'Existem {len(df_fare_outliers_superiores)} outliers superiores')
    print(f'Existem {len(df_fare_outliers_inferiores)} outliers inferiores')
print('\n------------------------------------\n')