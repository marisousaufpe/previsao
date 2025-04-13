#%% 

import pandas as pd
import os

nome_projeto = 'previsao'


def obter_dados_de_arquivo(nome_arquivo):

    """
    Esta função lê os dados de um arquivo ".parquet" e os retorna.

    Args:
        nome_arquivo (str): nome do arquivo .parquet que será buscado na pasta "dados/".

    Returns:
        pandas.DataFrame: Uma tabela de dados (DataFrame) lida do arquivo.
                          Retorna None se houver algum erro ao ler o arquivo.
    """

    """
    Este trecho garante que o script volte uma pasta e entre na pasta dados/
    """
    #caminho_arquivo = os.path.dirname(os.path.abspath(__file__)) # Retorna o diretório sem o nome do arquivo do script
    #caminho_arquivo = os.path.basename(caminho_arquivo) # Retorna apenas o nome da última pasta
    #caminho_arquivo = os.getcwd().split(caminho_arquivo)[0] # Retira o nome da última pasta

    caminho_arquivo = os.getcwd().split(nome_projeto)[0] + nome_projeto + '/dados/' + nome_arquivo

    try:
        dados = pd.read_parquet(caminho_arquivo)
        print(f'Dados lidos com sucesso do arquivo: "{nome_arquivo}"')
        return dados
    except FileNotFoundError:
        print(f'Arquivo "{nome_arquivo}" não encontrado')
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo {e}")
        return None

#%%
if __name__ == "__main__":

    # Aqui é onde o script é executado se você rodar diretamente este arquivo
    nome_arquivo = '2020_macacos_cbr_tma.parquet'  # Assumindo que seu arquivo se chama assim
    dados_obtidos = obter_dados_de_arquivo(nome_arquivo)

    if dados_obtidos is not None:
        print("\nPrimeiras linhas dos dados obtidos:")
        print(dados_obtidos.head())  # Mostra as primeiras linhas da tabela de dados


