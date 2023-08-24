import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data.csv'
dados_mercado = pd.read_csv(url)
dados_mercado.head(5)
# print(dados_mercado)

url_2 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data_ponto_virgula.csv'
dados_ponto_virgula = pd.read_csv(url_2)
dados_ponto_virgula = dados_ponto_virgula.head(5)
print(dados_ponto_virgula)
print('1')

dados_sem_virgula = pd.read_csv(url_2, sep=';')
dados_sem_virgula.head(4)
# print(dados_sem_virgula)

dados_primeiras_linhas = pd.read_csv(url, nrows=5)
# print(dados_primeiras_linhas)

dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])
# print(dados_selecao)

dados_selecao.to_csv('clientes_mercado.csv', index=False)

clientes_mercado = pd.read_csv('clientes_mercado.csv')
# print(clientes_mercado)