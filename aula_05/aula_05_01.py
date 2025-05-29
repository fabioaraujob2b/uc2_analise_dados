import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados financeira.csv
endereco_dados = 'BASES\Titanic.csv'

# Criando o DataFrame financeira
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_titanic = df_titanic[['Name','Sex','Age','Fare','Survived']]

# Exibindo a base de dados financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_titanic)

# Criando o array do valor da passagem e da idade
array_titanic_fare = np.array(df_titanic["Fare"])
array_titanic_age = np.array(df_titanic["Age"])
array_titanic_survived = np.array(df_titanic["Survived"])

# Obtendo a média do valor da passagem e da idade
media_fare = np.mean(array_titanic_fare)
media_age = np.mean(array_titanic_age)

# Obtendo a mediana do valor da passagem e da idade
mediana_fare = np.median(array_titanic_fare)
mediana_age = np.median(array_titanic_age)

# Obtendo a distância entre a média e a mediana do valor da passagem e da idade
distancia_fare = abs((media_fare - mediana_fare) / mediana_fare)
distancia_age = abs((media_age - mediana_age) / mediana_age)

# Obtendo o máximo e o mínimo do valor da passagem e da idade
maximo_fare = np.max(array_titanic_fare)
maximo_age = np.max(array_titanic_age)
minimo_fare = np.min(array_titanic_fare)
minimo_age = np.min(array_titanic_age)

# Obtendo a amplitude do valor da passagem e da idade
amplitude_fare = maximo_fare - minimo_fare
amplitude_age = maximo_age - minimo_age

# obtendo os quartis do valor da passagem e da idade
q1_age = np.quantile(array_titanic_age, 0.25, method='weibull')
q2_age = np.quantile(array_titanic_age, 0.50, method='weibull')
q3_age = np.quantile(array_titanic_age, 0.75, method='weibull')
iqr_age = q3_age - q1_age

q1_fare = np.quantile(array_titanic_fare, 0.25, method='weibull')
q2_fare = np.quantile(array_titanic_fare, 0.50, method='weibull')
q3_fare = np.quantile(array_titanic_fare, 0.75, method='weibull')
iqr_fare = q3_fare - q1_fare

# Identificando os valores discrepantes - outliers da passagem e da idade
limite_superior_age = q3_age + (1.5 * iqr_age)
limite_inferior_age = q1_age - (1.5 * iqr_age)
limite_superior_fare = q3_fare + (1.5 * iqr_fare)
limite_inferior_fare = q1_fare - (15 * iqr_fare)

# Filtrando o dataframe dos valores discrepantes - outliers da passagem e da idade
df_age_outliers_superiores = df_titanic[df_titanic['Age'] > limite_superior_age]
df_age_outliers_inferiores = df_titanic[df_titanic['Age'] < limite_inferior_age]
df_fare_outliers_superiores = df_titanic[df_titanic['Fare'] > limite_superior_fare]
df_fare_outliers_inferior = df_titanic[df_titanic['Fare'] < limite_inferior_fare]

# Obtendo a quantidade de sobreviventes
qtd_passageiros = df_titanic['Survived'].count()
qtd_sobreviventes = df_titanic[df_titanic['Survived'] == 1].count()
percentual_sobreviventes = (qtd_sobreviventes / qtd_passageiros) * 100
df_titanic_survived = df_titanic[df_titanic['Survived'] == 1]

# Obtendo a quantidade total de homens e mulheres
qtd_masc = df_titanic[df_titanic['Sex'] == 'male'].count()
qtd_fem = df_titanic[df_titanic['Sex'] == 'female'].count()

# Obtendo a quantidade de homens e mulheres que sobreviveram
qtd_masc_sobre = df_titanic_survived[df_titanic_survived['Sex'] == 'male'].count()
qtd_fem_sobre = df_titanic_survived[df_titanic_survived['Sex'] == 'female'].count()

# Exibindo os dados sobre as idades dos passageiros
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS IDADES --")
print('Medidas de Tendência Central')
print(f"\nA média das idades é {media_age:.1f}")
print(f"A mediana das idades é {mediana_age:.1f}")
print(f"A distância entre a média e a mediana é {distancia_age}")
print(f"O menor valor das idades é {minimo_age}")
print(f"O maior valor das idades é {maximo_age}")
print(f"A amplitude dos valores das idades é {amplitude_age}")
print(f'O valor do 1º quartil - 25% do valor das idades: {q1_age}')
print(f'O valor do 2º quartil - 50% do valor das idades: {q2_age}')
print(f'O valor do 3º quartil - 75% do valor das idades: {q3_age}')
print(f'O valor do iqr das idades é: {iqr_age}')
print(f'O limite inferior do valor das idades é {limite_inferior_age}')
print(f'O limite Superior do valor das idades é {limite_superior_age}\n')

if len(df_age_outliers_inferiores) == 0:
    print('Não existem outliers inferiores')
else:
    print(df_age_outliers_inferiores)

if len(df_age_outliers_superiores) == 0:
    print('Não existem outliers inferiores')
else:
    print(df_age_outliers_superiores,'\n')

# Exibindo os dados sobre o valor das passagens
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS PASSAGENS --")
print('Medidas de Tendência Central')
print(f"\nA média das passagens é {media_fare:.2f}")
print(f"A mediana das passagens é {mediana_fare:.2f}")
print(f"A distância entre a média e a mediana é {distancia_fare}")
print(f"O menor valor das passagens é {minimo_fare:.2f}")
print(f"O maior valor das passagens é {maximo_fare:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_fare:.2f}")
print(f'O valor do 1º quartil - 25% do valor das passagens: {q1_fare}')
print(f'O valor do 2º quartil - 50% do valor das passagens: {q2_fare}')
print(f'O valor do 3º quartil - 75% do valor das passagens: {q3_fare}')
print(f'O valor do iqr das passagens é: {iqr_fare}')
print(f'O limite inferior do valor das passagens é {limite_inferior_fare}')
print(f'O limite Superior do valor das passagens é {limite_superior_fare}\n')

if len(df_fare_outliers_inferior) == 0:
    print('Não existem outliers inferiores')
else:
    print('Outliers inferiores das passagens')
    print(df_fare_outliers_inferior,'\n')
if len(df_fare_outliers_superiores) == 0:
    print('Não existem outliers superiores')
else:
    print('Outliers superiores das passagens')
    print(df_fare_outliers_superiores)

# Exibindo os dados sobre os sobreviventes
print("\n-- OBTENDO INFORMAÇÕES SOBRE OS SOBREVIVENTES --")
print(f"A quantidade de passageiros foi {qtd_passageiros}")
print(f"A quantidade de sobreviventes foi {qtd_sobreviventes.values[0]}")
print(f"O percentual de sobreviventes foi {percentual_sobreviventes.values[0]:.2f} %")
print(f"A quantidade de homens sobreviventes foi {qtd_masc_sobre.values[0]}")
print(f"A quantidade de mulheres sobreviventes foi {qtd_fem_sobre.values[0]}")

# Exibindo os dados sobre os passageiros
print("\n-- OBTENDO INFORMAÇÕES SOBRE OS PASSAGEIROS --")
print(f"A quantidade total de homens é {qtd_masc.values[0]}")
print(f"A quantidade total de mulheres é {qtd_fem.values[0]}")