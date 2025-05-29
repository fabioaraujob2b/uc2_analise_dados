import pandas as pd

n1 = pd.Series([12,22,33,44,55,66,77,88,99,100])
n2 = pd.Series([11,12,13,14,15,16,17,18,19,20])

print("Soma: ")
print(n1.add(n2))
print("Subtração: ")
print(n1 - n2)
print("Multiplicação: ")
print(n1.mul(n2))
print("Divisão: ")
print(n1.div(n2))