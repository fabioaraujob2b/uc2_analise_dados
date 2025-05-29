import pandas as pd 

vendedores = [
    ['Maria',800,700,1000,900,1200,600,600],
    ['João',900,500,1100,1000,900,500,700],
    ['Manuel',700,600,900,1200,900,700,400]
]

colunas =  ['Nome','Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

df_vendedores = pd.DataFrame(vendedores,columns=colunas)

print(df_vendedores)

soma_seg = df_vendedores['Segunda'].sum()
media_seg = df_vendedores['Segunda'].mean()
maior_seg = df_vendedores['Segunda'].max()
menor_seg = df_vendedores['Segunda'].min()
nome_vendedor_segunda = df_vendedores[df_vendedores['Segunda'] == maior_seg]['Nome'][1]
print(f'\nO vendedor que vendeu mais na Segunda-feira: {nome_vendedor_segunda}')