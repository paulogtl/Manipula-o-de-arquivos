# 2. Ler um Arquivo Linha por Linha
# O loop for line in arquivo: é a maneira mais eficiente em Python para iterar sobre as linhas de um arquivo.

def ler_linha_por_linha(nome_arquivo):
    """Lê e exibe o conteúdo de um arquivo linha por linha."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print(f"--- Conteúdo de '{nome_arquivo}' (linha por linha) ---")
            for numero_linha, linha in enumerate(arquivo, 1):
                # O método strip() remove espaços em branco/quebras de linha (\n)
                print(f"Linha {numero_linha}: {linha.strip()}")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

# Exemplo de uso:
# ler_linha_por_linha('meu_arquivo.txt')