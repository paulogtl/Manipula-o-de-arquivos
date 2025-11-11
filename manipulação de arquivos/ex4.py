#4. Adicionar Conteúdo ao Final de um Arquivo
#O modo de abertura 'a' (append) adiciona dados ao final do arquivo sem apagar o conteúdo existente.
def adicionar_conteudo(nome_arquivo, novo_conteudo):
    """Adiciona novo conteúdo ao final de um arquivo existente."""
    try:
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            # Garante que o conteúdo seja adicionado em uma nova linha
            arquivo.write('\n' + novo_conteudo)
        print(f"Sucesso: Conteúdo adicionado ao final de '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao adicionar conteúdo: {e}")

# Exemplo de uso:
# adicionar_conteudo('dados.txt', "Conteúdo adicionado por último.")