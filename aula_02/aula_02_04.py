import pandas as pd 

idades = pd.Series([1,12,36,33,44,52,69,47,99])

acima = idades[idades >= 18]
abaixo = idades[idades < 18]
print("Idades maiores e iguais a 18: ")
print(acima)
print("Idades menores a 18: ")
print(abaixo)
