import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


df = pd.read_csv('bases/base_dados_sorvete_clima.csv')


sns.set(style="whitegrid")


df['Data'] = pd.to_datetime(df['Data']).dt.strftime('%Y-%m-%d')

# Modelo de regressão
x = df[['Temperatura_Media']]
y = df['Producao_Sorvete']
modelo = LinearRegression().fit(x, y)
df['y_predito'] = modelo.predict(x)

# Criar figura
fig, axs = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Análise dos Dados - Produções de Sorvete e Temperaturas", fontsize=16)

# 1. Top 10 Produção - gráfico de barras horizontais com seaborn
top10_prod = df.sort_values(by="Producao_Sorvete", ascending=False).head(10)
sns.barplot(y='Data', x='Producao_Sorvete', data=top10_prod, ax=axs[0, 0], palette='Blues_d')
axs[0, 0].set_title("Top 10 Dias com Maior Produção de Sorvete")
axs[0, 0].set_xlabel("Litros Produzidos")
axs[0, 0].set_ylabel("Data")

# 2. Top 10 Temperatura
top10_temp = df.sort_values(by="Temperatura_Media", ascending=False).head(10)
sns.barplot(y='Data', x='Temperatura_Media', data=top10_temp, ax=axs[0, 1], palette='Reds_r')
axs[0, 1].set_title("Top 10 Dias com Maior Temperatura")
axs[0, 1].set_xlabel("Temperatura (°C)")
axs[0, 1].set_ylabel("Data")

# 3. Dispersão com seaborn
sns.scatterplot(x='Temperatura_Media', y='Producao_Sorvete', data=df, ax=axs[1, 0], color="purple")
axs[1, 0].set_title("Correlação: Temperatura vs Produção")
axs[1, 0].set_xlabel("Temperatura Média (°C)")
axs[1, 0].set_ylabel("Produção de Sorvete (litros)")

# 4. Regressão linear
sns.regplot(x='Temperatura_Media', y='Producao_Sorvete', data=df, ax=axs[1, 1],
            line_kws={"color": "darkred"}, scatter_kws={"color": "orange"})
axs[1, 1].set_title("Regressão Linear: Temperatura vs Produção")
axs[1, 1].set_xlabel("Temperatura Média (°C)")
axs[1, 1].set_ylabel("Produção de Sorvete (litros)")

# Ajustar layout
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('img/analise_sorvete_temperatura.png')
plt.show()