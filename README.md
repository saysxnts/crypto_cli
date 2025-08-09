# Ferramenta de Linha de Comando (CLI) para Preços de Criptomoedas

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.31-orange)

## 📖 Sobre o Projeto

Esta é uma ferramenta de linha de comando (CLI - Command-Line Interface) desenvolvida em Python que busca e exibe os preços em tempo real de múltiplas criptomoedas. Os dados são consumidos da API pública e gratuita da CoinGecko.

O projeto serve como um exercício prático para consumir APIs REST, processar dados JSON e interagir com o sistema operacional através de argumentos de linha de comando.

---

## ✨ Funcionalidades

- Busca de preços para uma ou mais criptomoedas em uma única chamada.
- Exibição dos preços em Dólar Americano (USD) e Real Brasileiro (BRL).
- Interface de linha de comando simples e direta.
- Tratamento de erros para moedas com IDs inválidos ou problemas de conexão com a API.

---

## 🛠️ Tecnologias e Conceitos Praticados

- **Python 3**
- **Biblioteca `requests`**: Para realizar requisições HTTP GET de forma simples e eficiente.
- **Módulo `sys`**: Para ler os argumentos passados na linha de comando.
- **Consumo de API REST**: Entendimento de como construir requisições com parâmetros e consumir os dados.
- **Parsing de JSON**: Conversão da resposta da API em um dicionário Python para fácil manipulação.
- **Tratamento de Exceções**: Uso de blocos `try...except` para lidar com erros de rede e HTTP.

---

## 🚀 Como Rodar a Ferramenta

### **Pré-requisitos**

- **Python 3**
- **pip** (gerenciador de pacotes do Python)

### **Instalação e Execução**

1.  **Clone o repositório**:
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Navegue até a pasta do projeto**:
    ```bash
    cd crypto_cli
    ```

3.  **Instale as dependências**:
    ```bash
    pip install requests
    ```

4.  **Execute o script** passando os IDs das moedas como argumentos. Os IDs podem ser encontrados no site da CoinGecko (geralmente o nome em minúsculo).
    ```bash
    # Exemplo com uma moeda
    python crypto_cli.py bitcoin

    # Exemplo com múltiplas moedas
    python crypto_cli.py cardano polkadot ethereum
    ```

### Exemplo de Saída
```
$ python crypto_cli.py bitcoin
Buscando preços para: bitcoin...
----------------------------------------
Bitcoin:
  USD: $68,123.00
  BRL: R$350,123.45
----------------------------------------
```

---

## ✒️ Autor

**Guilherme**
