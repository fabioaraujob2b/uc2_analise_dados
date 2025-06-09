import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

# Criando o DataFrame Homicídios Dolosos
df_hom_doloso = df_ocorrencias[['cisp','hom_doloso']]
df_hom_doloso = df_hom_doloso.groupby(['cisp']).sum(['hom_doloso']).reset_index()

# Criando o DataFrame Homicídios Culposos
df_hom_culposo = df_ocorrencias[['cisp','hom_culposo']]
df_hom_culposo = df_hom_culposo.groupby(['cisp']).sum(['hom_culposo']).reset_index()    

# Criando o DataFrame Homicídios Dolosos e Culposos
df_hom_doloso_culposo = df_ocorrencias[['cisp','hom_doloso','hom_culposo']]
df_hom_doloso_culposo = df_hom_doloso_culposo.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index()

# Criando o Array dos Homicídio Dolosos
array_hom_doloso = np.array(df_hom_doloso["hom_doloso"])

# Criando o Array dos Homicídio Culposos
array_hom_culposo = np.array(df_hom_culposo["hom_culposo"])

# IQR (Intervalo interquartil)
    # q3 - q1
    # É a amplitude do intervalo dos 50% dos dados centrais
    # Ela ignora os valores extremos. Max e Min que estão fora do IQR
    # Não sofre a interferência dos valores extremos
    # quanto mais próximo de zero, mais homogêneo são os dados
    # quanto mais próximo do q3, mais heterogêneo são os dados

# Obtendo os Quartis dos Homicídios Dolosos - Método weibull
q1_hom_doloso = np.quantile(array_hom_doloso, 0.25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso, 0.50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso, 0.75, method='weibull')
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso

# Obtendo os Quartis dos Homicídios Culposos - Método weibull
q1_hom_culposo = np.quantile(array_hom_culposo, 0.25, method='weibull')
q2_hom_culposo = np.quantile(array_hom_culposo, 0.50, method='weibull')
q3_hom_culposo = np.quantile(array_hom_culposo, 0.75, method='weibull')
iqr_hom_culposo = q3_hom_culposo - q1_hom_culposo  

# Identificando os outliers superiores e inferiores dos Homicídios Dolosos
limite_superior_hom_doloso = q3_hom_doloso + (1.5 * iqr_hom_doloso)
limite_inferior_hom_doloso = q1_hom_doloso - (1.5 * iqr_hom_doloso)

# Identificando os outliers superiores e inferiores dos Homicídios Culposos
limite_superior_hom_culposo = q3_hom_culposo + (1.5 * iqr_hom_culposo)
limite_inferior_hom_culposo = q1_hom_culposo - (1.5 * iqr_hom_culposo)

# Filtrando o DataFrame Homicídios Dolosos
df_hom_doloso_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] <= limite_superior_hom_doloso]
df_hom_doloso_outliers_inferiores = df_hom_doloso[df_hom_doloso['hom_doloso'] >= limite_inferior_hom_doloso]

# Filtrando o DataFrame Homicídios Culposos
df_hom_culposo_outliers_superiores = df_hom_culposo[df_hom_culposo['hom_culposo'] <= limite_superior_hom_culposo]
df_hom_culposo_outliers_inferiores = df_hom_culposo[df_hom_culposo['hom_culposo'] >= limite_inferior_hom_culposo]

# Verificando a existência de Outliers Inferiores para Homicídios Dolosos
print('\n- Verificando a existência de outliers inferiores - Homicídios Dolosos')
if len(df_hom_doloso_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_hom_doloso_outliers_inferiores)

# Verificando a existência de Outliers Inferiores para Homicídios Culposos
print('\n- Verificando a existência de outliers inferiores - Homicídios Culposos')
if len(df_hom_culposo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_hom_culposo_outliers_inferiores)

# Verificando a existência de Outliers Superiores para Homicídios Dolosos
print('\n- Verificando a existência de outliers superiores - Homicídios Dolosos')
if len(df_hom_doloso_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_hom_doloso_outliers_superiores)

# Verificando a existência de Outliers Superiores para Homicídios Culposos
print('\n- Verificando a existência de outliers superiores - Homicídios Culposos')
if len(df_hom_culposo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_hom_culposo_outliers_superiores)

# Correlação entre Homicídios Dolosos e Culposos
# 0.9 a 1.0 (positiva ou negativa) = Muito forte correlação
# 0.7 a 0.9 (positiva ou negativa) = Forte correlação
# 0.5 a 0.7 (positiva ou negativa) = Moderada correlação
# 0.3 a 0.5 (positiva ou negativa) = Fraca correlação
# 0.0 a 0.3 (positiva ou negativa) = Sem correlação

corr_hom_doloso_hom_culposo = np.corrcoef(df_hom_doloso_culposo['hom_doloso'], df_hom_doloso_culposo['hom_culposo'])[0,1]

print(f"Correlação entre Homicídios Dolosos e Culposos: {corr_hom_doloso_hom_culposo:.3f}") 

# Regressão Linear Simples
# Coeficiente angular: 
# Também chamado de inclinação da reta ou coeficiente de regressão, esse valor indica o quanto a variável dependente (por exemplo, vendas, temperatura, lucro etc.) aumenta ou diminui a cada unidade de aumento da variável independente (por exemplo, tempo, investimento, idade etc.).
# Intercepto:
# É o ponto onde a reta de regressão cruza o eixo Y. Representa o valor estimado da variável dependente quando a variável independente é zero.
# R²:
# Representa a proporção de variabilidade da variável dependente que pode ser explicada pela variável independente.
# É o coeficiente de determinação, que mede o quão bem o modelo explica a variação dos dados.
# Varia de 0 a 1:
# 0: o modelo não explica nada.
# 1: o modelo explica perfeitamente.

x_hom_doloso = df_hom_doloso_culposo[['hom_doloso']]
y_hom_culposo = df_hom_doloso_culposo[['hom_culposo']]
modelo_simples = LinearRegression()
modelo_simples.fit(x_hom_doloso, y_hom_culposo)
print("\nRegressão Linear Simples - Homicídios Dolosos e Culposos")
print(f"Coeficiente angular: {modelo_simples.coef_[0][0]:.2f}")
print(f"Intercepto: {modelo_simples.intercept_[0]:.2f}")
print(f"R²: {modelo_simples.score(x_hom_doloso, y_hom_culposo):.3f}")

# Visualizando os Dados Analisados
print('\n- Visualizando os Dados Analisados -')
plt.subplots(3,2,figsize=(16,10))
plt.suptitle('Análise dos Dados - Homicídios Dolosos e Culposos',fontsize=16)

# Posição 01: Gráfico dos Outliers dos Homicídios Dolosos
df_hom_doloso_outliers_superiores_order = df_hom_doloso_outliers_superiores.sort_values(by='hom_doloso',ascending=True)
df_hom_doloso_outliers_superiores_order = df_hom_doloso_outliers_superiores_order.head(10)
plt.subplot(3,2,1)
plt.title('Gráfico dos Outliers dos Homicídios Dolosos - Top 10',fontsize=14)
plt.barh(df_hom_doloso_outliers_superiores_order['cisp'].astype(str),df_hom_doloso_outliers_superiores_order['hom_doloso'])

# Posição 02: Gráfico dos Outliers dos Homicídios Culposos
df_hom_culposo_outliers_superiores_order = df_hom_culposo_outliers_superiores.sort_values(by='hom_culposo',ascending=True)
df_hom_culposo_outliers_superiores_order = df_hom_culposo_outliers_superiores_order.head(10)
plt.subplot(3,2,2)
plt.title('Gráfico dos Outliers dos Homicídios Culposos - Top 10',fontsize=14)
plt.barh(df_hom_culposo_outliers_superiores_order['cisp'].astype(str),df_hom_culposo_outliers_superiores_order['hom_culposo'])  

# Posição 03: Gráfico de Correlação dos Homicídios Dolosos e Culposos
plt.subplot(3,2,3)
plt.title('Gráfico de Correlação dos Homicídios Dolosos e Culposos',fontsize=14)
sns.scatterplot(x=df_hom_doloso_culposo['hom_doloso'], y=df_hom_doloso_culposo['hom_culposo'])

# Posição 04: Gráfico de Regressão Linear dos Homicídios Dolosos e Culposos
plt.subplot(3,2,4)
plt.title('Regressão Linear: Homicídios Dolosos e Culposos',fontsize=14)
sns.regplot(x="hom_doloso", y="hom_culposo",data=df_hom_doloso_culposo,fit_reg=True)

# Posição 05: Medidas Descritivas das Recuperações de Veículos
plt.subplot(3,2,5)
plt.title('Medidas Descritivas dos Homicídios Dolosos e Culposos',fontsize=14)
plt.axis('off')
plt.text(0.1,0.8,f'Correlação entre Homicídios Dolosos e Culposos: {corr_hom_doloso_hom_culposo:.3f}',fontsize=12)
plt.text(0.1,0.6,f'Coeficiente Angular: {modelo_simples.coef_[0][0]:.2f}',fontsize=12) 
plt.text(0.1,0.4,f'Intercepto: {modelo_simples.intercept_[0]:.2f}',fontsize=12)
plt.text(0.1,0.2,f'R²: {modelo_simples.score(x_hom_doloso, y_hom_culposo):.3f}',fontsize=12)

# Posição 06: 
plt.subplot(3,2,6)
plt.axis('off')

plt.show()