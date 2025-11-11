# 8. Ler um Arquivo CSV e Retornar os Dados como Lista de Dicionários
# Utilizamos o módulo nativo csv para lidar corretamente com a estrutura de arquivos CSV (valores separados por vírgula, ponto e vírgula, etc.). 
# O objeto csv.DictReader é ideal para retornar os dados no formato de lista de dicionários, onde as chaves são os nomes das colunas (cabeçalhos).
import csv

def ler_csv_para_dicionarios(nome_arquivo, delimitador=','):
    """
    Lê um arquivo CSV e retorna os dados como uma lista de dicionários.
    As chaves dos dicionários são os cabeçalhos das colunas.
    """
    dados = []
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            # DictReader usa a primeira linha como nomes das chaves (cabeçalhos)
            leitor = csv.DictReader(arquivo_csv, delimiter=delimitador)
            for linha in leitor:
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print(f"Erro: Arquivo CSV '{nome_arquivo}' não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler arquivo CSV: {e}")
        return []

# Exemplo de uso (assumindo que 'dados.csv' existe com cabeçalho):
"""
# Exemplo de conteúdo em 'dados.csv':
# Nome,Idade,Cidade
# Alice,30,Rio
# Bob,25,Sao Paulo
"""
# lista_dados = ler_csv_para_dicionarios('dados.csv', delimitador=',')
# print("\nDados do CSV como Lista de Dicionários:")
# for item in lista_dados:
#     print(item)
