# 
def escrever_conteudo(nome_arquivo, novo_conteudo):
    """Escreve novo conteúdo no arquivo, sobrescrevendo o que existia."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(novo_conteudo)
        print(f"Sucesso: O arquivo '{nome_arquivo}' foi sobrescrito.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

# Exemplo de uso:
# escrever_conteudo('dados.txt', "Este é o novo conteúdo.\nLinha dois agora.")