# 7. Copiar o Conteúdo de um Arquivo para Outro
# Usamos a biblioteca nativa shutil para esta operação, pois ela lida de forma mais robusta com arquivos binários e grandes volumes de dados.
import shutil
import os

def copiar_arquivo(origem, destino):
    """Copia o conteúdo do arquivo de origem para o arquivo de destino."""
    try:
        # A função copy copia o conteúdo e o modo do arquivo
        shutil.copy(origem, destino)
        print(f"Sucesso: Conteúdo copiado de '{origem}' para '{destino}'.")
    except FileNotFoundError:
        print(f"Erro: Arquivo de origem '{origem}' não encontrado.")
    except Exception as e:
        print(f"Erro ao copiar arquivo: {e}")

# Exemplo de uso:
# copiar_arquivo('dados.txt', 'copia_dados.txt')