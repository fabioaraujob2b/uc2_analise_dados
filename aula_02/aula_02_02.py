import pandas as pd 

nota1 = pd.Series([50,60,80,90,100,40,45,28,30,70])
maior = nota1[nota1 >= 70]
menor = nota1[nota1 < 70]

print(f"Média maiores ou igual a 70: ")
print(maior)
print(f"Média menores que 70: ")
print(menor)
