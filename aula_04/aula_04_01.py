import pandas as pd 
import numpy as np 

#Importando a base de dados
endereco_dados = 'bases\Funcionarios.csv'
#Criando o DataFrame Funcionários
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

#Criando um array para o salário
array_salario = np.array(df_funcionarios['Salário'])
array_idade = np.array(df_funcionarios['Idade'])
array_tempo_empresa = np.array(df_funcionarios['Tempo'])

media_salario = np.mean(array_salario)
maior_salario = np.max(array_salario)
menor_salario = np.min(array_salario)
nome_salario_maior = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Nome']
mediana_salario = np.median(array_salario)
distancia_salario = abs((media_salario - mediana_salario) / mediana_salario)



media_idade = np.mean(array_idade)
maior_idade = np.max(array_idade)
menor_idade = np.min(array_idade)
mediana_idade = np.median(array_idade)
distancia_idade = abs((media_idade - mediana_idade) / mediana_idade)
amplitude_idade = maior_idade - menor_idade
nome_antigo = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']
nome_novo = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']


media_tempo = np.mean(array_tempo_empresa)
maior_tempo = np.max(array_tempo_empresa)
menor_tempo = np.min(array_tempo_empresa)
amplitude_tempo = maior_tempo - menor_tempo
nome_tempo_maior = df_funcionarios[df_funcionarios['Tempo'] == maior_tempo]['Nome']
mediana_tempo = np.median(array_tempo_empresa)
distancia_tempo = abs((media_tempo - mediana_tempo) / media_tempo)


qtd_funcionarios = np.count_nonzero(array_idade)

#Exibindo as Métricas
print('\n-----------------------Tabela de Funcionários-----------------------\n')
print(df_funcionarios)
print('\n-----------------------Exibindo os Resultados Solicitados-----------------------\n')
print(f'A média salarial dos funcionários é {media_salario:.2f}.')
print(f'A média da idade dos funcionários é {media_idade:.2f}.')
print(f'O Funcionário com maior tempo de empresa possui {maior_tempo} anos.')
print(f'O Funcionário com menor tempo de empresa possui {menor_tempo} anos.')
print(f'A amplitude relativa ao tempo de emrpesa é {amplitude_tempo} anos.')
print(f'A média do tempo de empresa é {media_tempo:.0f} anos.')
print(f'{nome_antigo.values[0]} é o funcionário com mais idade na empresa, com {maior_idade} anos.')
print(f'{nome_novo.values[0]} é o funcionário com mais idade na empresa, com {menor_idade} anos.')
print(f'A mediana das idades dos funcionários é {mediana_idade:.0f} anos.')
print(f'A distância entre a média e a mediana dos funcionários é: {distancia_idade:.2f} anos.')
print(f'A amplitude relativa a idade dos funcionário da empresa é {amplitude_tempo} anos.')
print(f'A quantidade de funcionários na empresa é {qtd_funcionarios} funcionários.')
print(f'{nome_salario_maior.values[0]} tem o maior salário recebendo R$ {maior_salario:.2f}.')
print(f'{nome_tempo_maior.values[0]} o funcionário com maior tempo de empresa, com {maior_tempo} anos de empresa.')
print(f'A mediana dos salários é: {mediana_salario:.0f}')
print(f'A distância entre a média e a mediana do salário dos funcionários é: {distancia_salario:.2f}')
print(f'A mediana de tempo de empresa é: {mediana_tempo:.0f} anos.')
print(f'A distância entre a média e a mediana tempo de empresa dos funcionários: {distancia_tempo:.2f}')
