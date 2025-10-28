import random


def filtrar_palavras_5_letras(lista_palavras):
    """
    Filtra uma lista de palavras e retorna apenas aquelas que têm exatamente 5 letras.
    
    Args:
        lista_palavras (list): Lista de palavras para filtrar
        
    Returns:
        list: Lista contendo apenas as palavras com 5 letras
    """
    return [palavra for palavra in lista_palavras if len(palavra.strip()) == 5]

if __name__ == "__main__":
    # Lendo palavras do arquivo.txt
    try:
        with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
            palavras = arquivo.readlines()
        
        # Removendo espaços em branco e linhas vazias
        palavras = [palavra.strip() for palavra in palavras if palavra.strip()]
        
        # Filtrando palavras com 5 letras
        palavras_filtradas = filtrar_palavras_5_letras(palavras)
        
        # Removendo palavras duplicadas usando set e convertendo de volta para lista
        palavras_sem_duplicatas = list(dict.fromkeys(palavras_filtradas))
        
        # Salvando resultado em um novo arquivo
        with open('palavras_5_letras.txt', 'w', encoding='utf-8') as arquivo:
            for palavra in palavras_sem_duplicatas:
                arquivo.write(palavra + '\n')
        
        print(f"Total de palavras no arquivo: {len(palavras)}")
        print(f"Total de palavras com 5 letras (com duplicatas): {len(palavras_filtradas)}")
        print(f"Total de palavras com 5 letras (sem duplicatas): {len(palavras_sem_duplicatas)}")
        print("\nAs palavras com 5 letras (sem duplicatas) foram salvas no arquivo 'palavras_5_letras.txt'")
        
        # Mostrando as primeiras 10 palavras encontradas como exemplo
        print("\nPrimeiras 10 palavras encontradas:")
        for palavra in palavras_sem_duplicatas[:10]:
            print(palavra)
            
    except FileNotFoundError:
        print("Erro: O arquivo 'arquivo.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro: Ocorreu um erro ao processar o arquivo: {str(e)}")