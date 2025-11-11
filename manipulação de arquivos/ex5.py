# 5. Contar o Número de Linhas em um Arquivo
# A maneira mais eficiente é iterar sobre o arquivo e contar cada linha, sem carregar todo o seu conteúdo na memória de uma vez.
def contar_linhas(nome_arquivo):
    """Retorna o número total de linhas em um arquivo."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # list(arquivo) retorna uma lista de todas as linhas, mas usar sum()
            # ou um loop for é mais seguro para arquivos muito grandes.
            # O código abaixo itera sem carregar tudo de uma vez:
            contador = sum(1 for linha in arquivo)
            return contador
    except FileNotFoundError:
        return f"Erro: Arquivo '{nome_arquivo}' não encontrado."

# Exemplo de uso:
# num_linhas = contar_linhas('dados.txt')
# print(f"O arquivo 'dados.txt' tem {num_linhas} linhas.")