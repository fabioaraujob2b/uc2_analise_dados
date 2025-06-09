import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('bases/consumo_cerveja.csv')

# Regressão linear
X = df[['Temperatura']]
y = df['Consumo de Cerveja']
modelo = LinearRegression()
modelo.fit(X, y)
pred = modelo.predict(X)

# Métricas
correlacao = df['Temperatura'].corr(df['Consumo de Cerveja'])
coef_angular = modelo.coef_[0]
intercepto = modelo.intercept_
r2 = modelo.score(X, y)

# Gráfico
fig, axs = plt.subplots(3, 2, figsize=(15, 8))
fig.suptitle('Análise dos Dados - Temperaturas e Consumo de Cervejas', fontsize=14)

# 1. Série histórica da temperatura
axs[0, 0].plot(df['Data'], df['Temperatura'])
axs[0, 0].set_title('Gráfico da Série Histórica das Temperaturas')

# 2. Série histórica do consumo
axs[0, 1].plot(df['Data'], df['Consumo de Cerveja'])
axs[0, 1].set_title('Gráfico da Série Histórica do Consumo de Cervejas')

# 3. Gráfico de correlação
sns.scatterplot(x='Temperatura', y='Consumo de Cerveja', data=df, ax=axs[1, 0])
axs[1, 0].set_title('Gráfico de Correlação das Temperaturas e Consumo')

# 4. Gráfico com regressão
sns.regplot(x='Temperatura', y='Consumo de Cerveja', data=df, ax=axs[1, 1], line_kws={'color': 'blue'})
axs[1, 1].set_title('Regressão Linear: Temperaturas e Consumo')

# 5. Gráfico de barras por tipo de tempo
tempo_consumo = df.groupby('Tempo')['Consumo de Cerveja'].sum().reindex(['sol', 'chuva', 'nublado', 'ensolarado'])
axs[2, 0].bar(tempo_consumo.index, tempo_consumo.values)
axs[2, 0].set_title('Gráfico de Barras de Tempo e Consumo')

# 6. Métricas descritivas como texto
axs[2, 1].axis('off')
texto = f"""
Medidas Descritivas das Temperaturas e Consumo de Cervejas

Correlação entre Temperatura e Consumo de Cerveja: {correlacao:.3f}
Coeficiente Angular: {coef_angular:.2f}
Intercepto: {intercepto:.2f}
R²: {r2:.3f}
"""
axs[2, 1].text(0, 0.5, texto, fontsize=10, va='center')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('img/consumo_ceverja.png')
plt.show()