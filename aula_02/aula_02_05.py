import pandas as pd 

def formatar(valor):
    return "{:.2f} %".format(valor)


roubo_automoveis = pd.Series([100,90,80,120,110,90,70], index = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'])
furto_automoveis = pd.Series([80,60,70,60,100,50,30], index = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'])
recuperacao = pd.Series([70,50,90,80,100,70,50], index = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'])

tx_tec = ((recuperacao.div(roubo_automoveis + furto_automoveis)) * 100).apply(formatar)

print(f"Quantida de roubos e furtos nos último 7 dias:\n{roubo_automoveis.add(furto_automoveis)}")
print(f"A taxa de recuperação de automoveis nos últimos 7 dias:\n{tx_tec}")

