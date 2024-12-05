import pandas as pd  #Importando a biblioteca pandas e apelidando de pd

tabela_vendas = pd.read_excel("Vendas.xlsx") # Importando a base de dados e criando a tabela de vendas e armazenando ela em uma variável 
# print(tabela_vendas) # Testando 

pd.set_option('display.max.columns', None) # Exibindo todas as colunas 
# print(tabela_vendas) #Testando 


# importar a base de dados
 
# visualizar base de dados 
 
# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
# print(faturamento) #tabela de faturamento por loja

# quantidade de produtos vendidos por lojas 
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
# print(quantidade) # quantidade vendida por loja 

# ticket medio por produto em cada loja 

# enviar um email com o relatório 