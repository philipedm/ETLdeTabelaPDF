# Antes é necessário instalar o pandas e o tabula-py
# pip install pandas
# pip install tabula-py

# importando pandas e tabula
import pandas as pd 
import tabula

arquivo = input("Digite o nome do arquivo PDF sem a extensão: ") 

# usa a biblioteca tabula para buscar as tabelas no pdf
lista_tabelas = tabula.read_pdf(arquivo + '.pdf', pages='all')

# cria uma nova tabela com as colunas
nova_tabela = pd.DataFrame({"codigo":{}, "preco":{}})

# estrutura de repeticao para acessar cada tabela
for tabela in lista_tabelas:
    # seleciono as colunas que preciso: primeira e penultima
    tabela = tabela.iloc[:, [0, -2]]

    # guarda os valores existentes nas colunas
    linha_aux = tabela.columns

    # adicionar os dados de linha_aux no dataframe nova_tabela
    nova_tabela = nova_tabela.append({"codigo":linha_aux[0], "preco":linha_aux[1]}, ignore_index=True)

    # renomeio as colunas da tabela
    tabela.columns = ["codigo", "preco"]

    # adiciono as linhas restantes na nova_tabela
    nova_tabela = nova_tabela.append(tabela[0:], ignore_index=True)
    
# tratando tabela para retirar alguns dados desnecessários
tabela_tratada = nova_tabela.query("codigo != 'CODIGO' & codigo != 'Unnamed: 0'")

# convertendo a coluna codigo para string
tabela_tratada["codigo"] = tabela_tratada["codigo"].astype(str)

# convertendo a coluna preco para float
tabela_tratada["preco"] = tabela_tratada["preco"].astype(float)

# criando excel com o arquivo final
tabela_tratada.to_excel("codigo_e_preco.xlsx", index=False)