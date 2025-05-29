import pandas as pd
import numpy as np

df_dados = 'bases\ENEM_2014_2023.csv'
df_enem = pd.read_csv(df_dados, sep=';', encoding='utf-8')
df_enem = df_enem[['Estado', 'Total']]
df_enem_top_10 = df_enem.sort_values(by='Total', ascending=False).head(10).to_string(index=False)

print("\n-- OBTENDO INFORMAÇÕES SOBRE O ENEM --\n")
print(df_enem.to_string(index=False),'\n')
print("\n-- OBTENDO O TOPO 10 DOS ESTADOS COM MAIOR NUMERO DE INSCRITOS NO ENEM --\n")
print(df_enem_top_10,'\n')

array_enem = np.array(df_enem['Total'])

#A média dos inscritos no exame dos últimos anos (2014 a 2023)
media_inscritos = np.mean(array_enem)
print(f"A média dos inscritos no exame dos últimos anos (2014 a 2023) é {media_inscritos:.2f}.")

#A mediana dos inscritos no exame dos últimos anos (2014 a 2023)
mediana_inscritos = np.median(array_enem)
print(f"A mediana dos inscritos no exame dos últimos anos (2014 a 2023) é {mediana_inscritos:.2f}.")

#A distancia entre a média e a mediana dos inscritos no exame dos últimos anos (2014 a 2023)
distancia_inscritos = abs((media_inscritos - mediana_inscritos) / media_inscritos)
print(f"A distancia entre a média e a mediana dos inscritos no exame dos últimos anos (2014 a 2023) é {distancia_inscritos:.2f}.")

#O maior e o menor número dos inscritos no exame dos últimos anos (2014 a 2023), assim com a amplitude dos valores
maior_numeros_incritos = np.max(array_enem)
menor_numeros_incritos = np.min(array_enem)
amplitude_inscritos = maior_numeros_incritos - menor_numeros_incritos

print(f"O maior número dos inscritos no exame dos últimos anos (2014 a 2023) é {maior_numeros_incritos}.")
print(f"O menor número dos inscritos no exame dos últimos anos (2014 a 2023) é {menor_numeros_incritos}.")    
print(f"A amplitude dos valores dos inscritos no exame dos últimos anos (2014 a 2023) é {amplitude_inscritos}.")

#Verifique se existem valores discrepantes (Outliers inferiores e/ou Superiores)
q1_inscritos = np.quantile(array_enem, 0.25, method='weibull')
q3_inscritos = np.quantile(array_enem, 0.75, method='weibull')
iqr_inscritos = q3_inscritos - q1_inscritos
limite_inferior_inscritos = q1_inscritos - (1.5 * iqr_inscritos)
limite_superior_inscritos = q3_inscritos + (1.5 * iqr_inscritos)

print(f"O limite inferior dos inscritos no exame dos últimos anos (2014 a 2023) é {limite_inferior_inscritos:.2f}.")
print(f"O limite Superior dos inscritos no exame dos últimos anos (2014 a 2023) é {limite_superior_inscritos:.2f}.")

df_enem_inferiores = df_enem[df_enem['Total'] < limite_inferior_inscritos]
df_enem_superiores = df_enem[df_enem['Total'] > limite_superior_inscritos]

if len(df_enem_inferiores) == 0:
    print('Não existem outliers inferiores')
else:
    print(df_enem_inferiores)
if len(df_enem_superiores) == 0:
    print('Não existem outliers superiores')
else:
    print(df_enem_superiores)
#Sabendo que o estado de Roraima possui o menor número de inscritos e o estado de São Pualo o maior número de inscritos no exame dos útimos anos, apresente o percentual de variação entre esses dois estados.
df_enem_roraima = df_enem[df_enem['Estado'] == 'Roraima']
df_enem_sao_paulo = df_enem[df_enem['Estado'] == 'São Paulo']
percentual = (df_enem_roraima['Total'].values[0] - df_enem_sao_paulo['Total'].values[0]) / df_enem_sao_paulo['Total'].values[0]
print(f"O percentual de variação entre os estados de Roraima e Sao Paulo é {percentual:.2f}%")