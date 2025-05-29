import pandas as pd 

def formatar(valor):
    return "{:.2f} %".format(valor)

ocorrencias = [ 
    ['Rio de Janeiro',6775561,35000], 
    ['Niteroi',515317,2500], 
    ['São Gonçalo',1091737,15000], 
    ['Duque de Caxias',924624,12000], 
    ['Nova Iguaçu',821128,10000], 
    ['Belford Roxo',513118,9000], 
    ['São João de Meriti',471906,8500], 
    ['Petrópolis',306678,1000], 
    ['Volta Redonda',273988,2000], 
    ['Campos dos Goytacazes',507548,4000], 
]

colunas = ['Municipio', 'População', 'Roubos']

df_dados = pd.DataFrame(ocorrencias, columns=colunas)

total_roubos = df_dados['Roubos'].sum()
media_roubos = df_dados['Roubos'].mean()
total_populacao = df_dados['População'].sum()
media_populacao = df_dados['População'].mean()
menor_qtd_roubo = df_dados['Roubos'].min()
maior_qtd_roubo = df_dados['Roubos'].max()
menor_qtd_populacao = df_dados['População'].min()
maior_qtd_populacao = df_dados['População'].max()

municipio_maior_indice = df_dados[df_dados['Roubos'] == maior_qtd_roubo]['Municipio']
municipio_menor_indice = df_dados[df_dados['Roubos'] == menor_qtd_roubo]['Municipio']
municipio_qtd_maior = df_dados[df_dados['População'] == maior_qtd_populacao]['Municipio']
municipio_qtd_menor = df_dados[df_dados['População'] == menor_qtd_populacao]['Municipio']

tx_roubos = ((df_dados['Roubos'] / df_dados['População']) * 100).apply(formatar)

print(f'O total de roubos no Estado do Rio de Janeiro: {total_roubos}')
print(f'A média de roubos no Estado do Estado do Rio de Janeiro: {media_roubos}')
print(f'O total da população no Estado do Rio de Janeiro: {total_populacao}')
print(f'A média da população no Estado do Rio de Janeiro: {media_populacao}')
print(f'O maior valor encontrado referente a roubo de pedestre: {maior_qtd_roubo}')
print(f'O menor valor encontrado referente a roubo de pedestre: {menor_qtd_roubo}')
print(f'O maior valor econtrado em realção a população: {maior_qtd_populacao}')
print(f'O menor valor econtrado em realção a população: {menor_qtd_populacao}')
print(f'O município com o maior índice de roubos a pedreste: {municipio_maior_indice.values[0]}')
print(f'O município com o menor índice de roubos a pedreste: {municipio_menor_indice.values[0]}')
print(f'O município com a maior população: {municipio_qtd_maior.values[0]}')
print(f'O município com a menor população: {municipio_qtd_menor.values[0]}')
print("------Taxa de roubos------")
print(df_dados['Municipio'] +" - "+ tx_roubos)