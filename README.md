# Zebrinha Azul Data Pipeline

## Desafio de Engenheiro de Dados Júnior - Zebrinha Azul

Este repositório contém a solução para o desafio prático de Engenheiro de Dados Júnior da Zebrinha Azul. O projeto envolve a extração, transformação e carga (ETL) de dados de clima e trânsito, bem como a criação de visualizações interativas para explorar esses dados.

## Pré-requisitos

- Python 3.x
- MySQL
- Bibliotecas Python (listadas em `requirements.txt`)

## Configuração do Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/ismaelbarrospbi/zebrinha-azul-data-pipeline.git
   cd zebrinha-azul-data-pipeline

## Decisões Técnicas, Escolhas e Requisitos

### Decisões Técnicas

- **Linguagem e Framework**: Optei por utilizar Python devido à sua ampla adoção e flexibilidade para processamento de dados. O Pandas foi escolhido para manipulação de dados tabulares devido às suas funcionalidades robustas e eficiência.

- **Arquitetura**: O projeto foi estruturado com base na abordagem ETL (Extract, Transform, Load), garantindo separação de responsabilidades e facilitando a manutenção e escalabilidade do sistema.

- **Banco de Dados**: Utilizei MySQL para armazenar os dados transformados devido à sua confiabilidade, suporte a consultas complexas e escalabilidade.

### Escolhas

- **APIs Utilizadas**: A API do OpenWeatherMap para dados de clima devido à sua cobertura global e precisão. A API do Google Maps Directions foi selecionada para dados de tráfego devido à sua capacidade de fornecer informações detalhadas de rotas.

- **Formato de Saída**: Optei por gerar arquivos CSVs para os dados transformados, facilitando análise e visualização dos dados fora do ambiente de banco de dados.

### Requisitos

- **Configuração do Ambiente**: Para configurar o ambiente de desenvolvimento, siga as instruções no arquivo README.md, incluindo a instalação de dependências listadas no requirements.txt e configuração das chaves de API necessárias.

- **Execução do Projeto**: Para executar o projeto localmente, certifique-se de ativar um ambiente virtual, configurar as variáveis de ambiente e executar os scripts `main.py` e `load_data.py` na ordem correta para extrair, transformar e carregar os dados.


Estratégia de Testes
Incluímos uma estratégia abrangente de testes para garantir a qualidade e a integridade do código. A seguir estão os tipos de testes implementados e as ferramentas utilizadas:

Tipos de Testes:

Testes Unitários: Testamos unidades individuais de código para verificar se funcionam como esperado isoladamente.
Testes de Integração: Verificamos a integração entre diferentes componentes do sistema para garantir que se comuniquem corretamente.
Testes de Regressão: Garantimos que as alterações no código não introduzam regressões em funcionalidades existentes.
Ferramentas Utilizadas:

Utilizamos pytest como framework principal para testes de unidade e integração devido à sua simplicidade e poderosas capacidades de teste.
Unittest foi utilizado em conjunto com pytest para testes de integração e para garantir a cobertura completa de código.
Execução de Testes Localmente:

Para executar os testes localmente, siga estes passos:
Configuração do Ambiente: Certifique-se de que todas as dependências estão instaladas. Você pode instalá-las usando pip install -r requirements.txt.
Execução dos Testes: No terminal, execute o seguinte comando:

pytest

Análise de Resultados: Após a execução dos testes, analise os resultados exibidos no terminal para verificar se todos os testes passaram com êxito.

