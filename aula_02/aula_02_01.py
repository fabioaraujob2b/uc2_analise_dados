nota1 = [50,60,80,90,100,40,45,28,30,70]
maior = []
menor = []

for i in range(len(nota1)):
    if nota1[i] >= 70:
        maior.append(nota1[i])
    else:
        menor.append(nota1[i])

print(f"Média maiores ou igual a 70: {maior}")
print(f"Média menores que 70: {menor}")
