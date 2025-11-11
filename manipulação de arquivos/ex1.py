# 1. Ler Todo o Conteúdo de um Arquivo de Texto
# A função read() é usada para ler o conteúdo inteiro do arquivo como uma única string.

def ler_conteudo_completo(nome_arquivo):
    """Lê e retorna todo o conteúdo de um arquivo de texto."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        return f"Erro: Arquivo '{nome_arquivo}' não encontrado."

# Exemplo de uso:
# print(ler_conteudo_completo('meu_arquivo.txt'))