# crypto_cli.py

import sys
import requests
import json

# URL base da API da CoinGecko que usaremos
API_URL = "https://api.coingecko.com/api/v3/simple/price"

def buscar_precos(ids_moedas):
    """
    Busca os preços das moedas fornecidas na API da CoinGecko.
    'ids_moedas' deve ser uma lista de strings, ex: ['bitcoin', 'ethereum']
    """
    # A API espera os IDs separados por vírgula
    ids_string = ",".join(ids_moedas)

    # Parâmetros da nossa requisição: os ids das moedas e as moedas para comparação (dólar e real)
    params = {
        'ids': ids_string,
        'vs_currencies': 'usd,brl'
    }

    try:
        # Faz a requisição GET para a API
        response = requests.get(API_URL, params=params)
        # Lança um erro se a resposta não for bem-sucedida (ex: erro 404, 500)
        response.raise_for_status()

        # Converte a resposta JSON em um dicionário Python
        return response.json()

    except requests.exceptions.HTTPError as errh:
        print(f"Erro HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Erro de Conexão: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Erro de Timeout: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Ocorreu um erro: {err}")

    return None

def exibir_precos(dados_precos, ids_moedas):
    """Formata e exibe os preços das moedas."""
    if not dados_precos:
        print("Não foi possível obter os dados dos preços.")
        return

    print("-" * 40)
    for moeda in ids_moedas:
        # Verifica se a API retornou dados para a moeda solicitada
        if moeda in dados_precos:
            preco_usd = dados_precos[moeda].get('usd', 'N/A')
            preco_brl = dados_precos[moeda].get('brl', 'N/A')
            # O .capitalize() deixa a primeira letra maiúscula
            print(f"{moeda.capitalize()}:")
            print(f"  USD: ${preco_usd:,.2f}") # Formata com vírgulas e 2 casas decimais
            print(f"  BRL: R${preco_brl:,.2f}")
            print("-" * 40)
        else:
            print(f"Não foi possível encontrar o preço para '{moeda}'.")
            print("Verifique se o ID da moeda está correto.")
            print("-" * 40)


# Ponto de entrada do script
if __name__ == "__main__":
    # sys.argv é uma lista de argumentos da linha de comando.
    # sys.argv[0] é o nome do script ('crypto_cli.py')
    # sys.argv[1:] são todos os argumentos seguintes (os nomes das moedas)

    if len(sys.argv) < 2:
        print("Uso: python crypto_cli.py <id_moeda_1> <id_moeda_2> ...")
        print("Exemplo: python crypto_cli.py bitcoin ethereum solana")
        # sys.exit() para o script se nenhum argumento for passado
        sys.exit(1)

    ids_das_moedas_para_buscar = sys.argv[1:]

    print(f"Buscando preços para: {', '.join(ids_das_moedas_para_buscar)}...")

    precos = buscar_precos(ids_das_moedas_para_buscar)
    exibir_precos(precos, ids_das_moedas_para_buscar)