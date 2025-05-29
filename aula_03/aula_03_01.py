import pandas as pd

def formatar(valor):
    return "{:.2f}%".format(valor)

populacao_vacinada = pd.Series([30000000, 25000000, 10000000, 5000000], index = ['2021', '2022', '2023', '2024'])
populacao_total = pd.Series([213317639, 214477744, 215574303, 216687971], index = ['2021', '2022', '2023', '2024'])

taxa_vacinacao_anual = (populacao_vacinada.div(populacao_total) * 100).apply(formatar)
total_vacinacao = (populacao_vacinada.sum()/populacao_total.tail(1).iloc[0]) * 100

print(f'A média de pessoas vacinadas: {populacao_vacinada.mean()}')
print(f'O total de pessoas vacinadas: {populacao_vacinada.sum()}')
print(f'O total da população no Brasil: {populacao_total.sum()}')
print(f'A média da população Brasileira: {populacao_total.mean()}\n')
print(f'O total de vacinação: {total_vacinacao:.0f}%')
print(f'A taxa anual de vacinação nos últimos 4 anos:\n{taxa_vacinacao_anual}')