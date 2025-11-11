# 6. Buscar uma Palavra em um Arquivo e Exibir as Linhas Onde Ela Aparece
# Esta função itera linha por linha e verifica se a palavra de busca está presente, desconsiderando a capitalização (opcionalmente).
def buscar_palavra(nome_arquivo, palavra_busca):
    """Busca uma palavra e exibe as linhas onde ela foi encontrada."""
    linhas_encontradas = []
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for num_linha, linha in enumerate(arquivo, 1):
                # Converte para minúsculas para uma busca que não diferencia maiúsculas/minúsculas
                if palavra_busca.lower() in linha.lower():
                    linhas_encontradas.append((num_linha, linha.strip()))
        
        if linhas_encontradas:
            print(f"\n--- Palavra '{palavra_busca}' encontrada em '{nome_arquivo}': ---")
            for num, linha_conteudo in linhas_encontradas:
                print(f"Linha {num}: {linha_conteudo}")
        else:
            print(f"\nPalavra '{palavra_busca}' não encontrada no arquivo.")
            
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

# Exemplo de uso:
# buscar_palavra('dados.txt', 'conteúdo')