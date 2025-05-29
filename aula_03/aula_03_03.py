# Importando a Biblioteca
import pandas as pd

# Criando a Tabela Vendedor
vendedores = [ 
    ['Ana','F',28,120], 
    ['Bruno','M',34,150],
    ['Carlos','M',45,110], 
    ['Diana','F',30,95], 
    ['Eduardo','M',40,130], 
    ['Fernanda','F',29,140], 
    ['Gustavo','M',38,105], 
    ['Helena','F',31,125], 
    ['Igor','M',27,100], 
    ['Juliana','F',33,135], 
]

# Criando as Colunas da Tabela Vendedor
colunas = ['Nome','Sexo','Idade','Vendas']

# Criando o dataFrame Vendedor
df_vendedores = pd.DataFrame(vendedores,columns=colunas)

# Realizando as Métricas Solicitadas
soma_vendas = df_vendedores['Vendas'].sum()
media_vendas = df_vendedores['Vendas'].mean()
media_idade = df_vendedores['Idade'].mean()
maior_idade = df_vendedores['Idade'].max()
menor_idade = df_vendedores['Idade'].min()
maior_vendas = df_vendedores['Vendas'].max()
menor_vendas = df_vendedores['Vendas'].min()
melhor_vendedor = df_vendedores[df_vendedores['Vendas'] == maior_vendas]['Nome']
pior_vendedor = df_vendedores[df_vendedores['Vendas'] == menor_vendas]['Nome']
vendas_fem = df_vendedores[df_vendedores['Sexo'] == 'F']['Vendas'].sum()
vendas_masc = df_vendedores[df_vendedores['Sexo'] == 'M']['Vendas'].sum()

# Exibindo o DataFrame Vendedores
print('\n----------- Tabela Vendedores --------')
print(df_vendedores)
print('\n--------- Medidas Descritivas ----------')
print(f'A quantidade total de vendas foi {soma_vendas}')
print(f'A quantidade média de vendas foi {media_vendas:.0f}')
print(f'A média de idade dos vendedores é {media_idade:.0f}')
print(f'A maior idade encontrada foi {maior_idade}')
print(f'A menor idade encontrada foi {menor_idade}')
print(f'A quantidade total de vendas realizada pelas vendedoras foi {vendas_fem}')
print(f'A quantidade total de vendas realizada pelos vendedores foi {vendas_masc}')
print(f'Sr(a) {melhor_vendedor.values[0]} vendeu {maior_vendas} produtos, tendo o melhor desempenho')
print(f'Sr(a) {pior_vendedor.values[0]} vendeu {menor_vendas} produtos, tendo o pior desempenho')