# GET<i>Var</i> 🧬👨🏻‍💻

O **GET<i>Var</i>** é uma ferramenta desenvolvida para **análise e anotação de variantes genéticas**. Com um workflow eficiente, a ferramenta integra dados de variantes genômicas para identificar e interpretar anotações de variantes de forma rápida e precisa em bancos de dados públicos.

## Funcionalidades

- **Análise de Variantes**: Processamento e visualização dados de variantes genéticas.
- **Anotação Funcional**: Integração de variantes com consulta em bancos de dados genéticos.
- **Automatização**: Workflow padronizado para maior eficiência.

## Workflow da Aplicação

1. **Entrada de Dados**:

   - Apenas arquivos **VCF** são válidos como entrada.

2. **Identificação de Variantes**:

   - A aplicação faz anotações com os seguintes campos:
     - **ID**: Identificador único da variante no banco de dados de referência.
     - **CHROM**: Cromossomo onde a variante está localizada.
     - **REF**: Alelo de referência no genoma.
     - **ALT**: Alelo alternativo identificado.
     - **Population Allele Frequency**: Frequência da variante em populações conhecidas.
     - **Var Class**: Classe da variante, como SNV (Single Nucleotide Variant) ou INDEL.
     - **Most Severe Consequence**: Consequência mais grave da variante em relação à função do gene.
     - **Clinical Significance**: Relevância clínica da variante com base em dados de referência.
     - **Synonyms**: Nomes alternativos ou identificadores da variante.
     - **Ambiguity**: Nível de ambiguïdade na identificação da variante.
     - **Minor Allele**: Alelo menos frequente encontrado na população.
     - **Mappings**: Informações adicionais de diferentes bancos e referências genômicas.

   - Os bancos consultados incluem **dbSNP**, **Ensembl** e **ClinVar**.

3. **Anotação Funcional**:

   - Integração com bancos de dados como dbSNP, ClinVar e Ensembl para fornecer informações funcionais e clínicas sobre as variantes.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: Snakemake, Bootstrap e Flask
- **Bancos de Dados**: Integrações com dbSNP, ClinVar e Ensembl

## Estrutura do Projeto

- **`main.py`**: Arquivo principal para executar a aplicação.
- **`api_getters.py`**: Contém funções para integrar e buscar dados externos.
- **`views.py`**: Gerencia as rotas e interações do usuário.
- **`utils.py`**: Arquivo com funções auxiliares para processamento de dados.
- **`Snakefile`**: Define os workflows automatizados usando Snakemake para gerenciar pipelines de análise.
- **`templates/`**: Arquivos HTML para visualização de resultados.
- **`static/`**: Arquivos de imagens e vídeos usados pela aplicação.
  - **`images/`**: Contém ícones, logos e outras imagens.
  - **`videos/`**: Contém vídeos ilustrativos ou de demonstração.
- **`requirements.txt`**: Lista de dependências necessárias para o projeto.
- **`.gitignore`**: Arquivo para ignorar arquivos e diretórios desnecessários no controle de versão.
- **`LICENSE`**: Arquivo contendo a licença do projeto.

## Requisitos de Instalação

Certifique-se de ter as seguintes ferramentas instaladas:

- Python >= 3.8
- Gerenciador de pacotes `pip`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/madsondeluna/getvar_containerized.git
   cd getvar_containerized
   ```

2. Crie um ambiente virtual (opcional, mas é recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale o Snakemake:

   ```bash
   pip install snakemake
   ```

## Execução

1. Execute o snakemake:
 ```bash
   snakemake
   ```

2. Acesse a aplicação no navegador em:
 ```
   http://localhost:5000
   ```

## Exemplo de Uso

Submeta um arquivo **VCF** através da interface web. O sistema processará os dados, realizará as anotações e disponibilizará um relatório final em formato tabular que pode ser filtrada através das respectivas anotações. 

## Informaçõs Adicionais de Uso 

As APIs REST do dbSNP, ClinVar e Ensembl possuem um limite de até 30 requisições por solicitação. Por isso, a aplicação pode apresentar instabilidade ou lentidão em alguns momentos. Além disso, os servidores dessas plataformas ocasionalmente podem ficar instáveis ou não responder adequadamente às requisições. Nesses casos, o manual das APIs recomenda a resubmissão dos dados para completar o processo de anotação.

## Docker

### Instalação e Uso

Para construir e executar a aplicação usando Docker, siga os passos abaixo:

1. Certifique-se de ter o Docker instalado em sua máquina. Você pode baixar e instalar o Docker a partir do [site oficial](https://www.docker.com/get-started).

2. Clone o repositório:

   ```bash
   git clone https://github.com/madsondeluna/getvar_containerized.git
   cd getvar_containerized
   ```

3. Construa a imagem Docker:

   ```bash
   docker build -t getvar_containerized .
   ```

4. Execute o contêiner Docker:

   ```bash
   docker run -p 5000:5000 getvar_containerized
   ```

5. Acesse a aplicação no navegador em:

   ```
   http://localhost:5000
   ```

## Como Colaborar

Se você deseja colaborar com este projeto, siga os passos abaixo:

1. Faça um fork do repositório.

2. Crie uma nova branch para a sua feature ou correção de bug:

   ```bash
   git checkout -b minha-feature
   ```

3. Faça as alterações necessárias e commit:

   ```bash
   git commit -m "Adiciona minha feature"
   ```

4. Envie as alterações para o seu repositório forkado:

   ```bash
   git push origin minha-feature
   ```

5. Abra um Pull Request no repositório original.

## Solução de Problemas

Se você encontrar algum problema ao executar o aplicativo, considere as seguintes etapas de solução de problemas:

1. **Aplicativo Flask Não Inicia**:
   - Certifique-se de que o arquivo `main.py` está configurado corretamente com `host='0.0.0.0'` e `port=5000`.
   - Verifique se há erros de sintaxe ou dependências ausentes no arquivo `main.py`.

2. **Erros na Construção da Imagem Docker**:
   - Verifique se os arquivos `Dockerfile` e `docker-compose.yml` estão configurados corretamente.
   - Certifique-se de que todas as dependências necessárias estão listadas no arquivo `requirements.txt`.

3. **Problemas no Workflow do Snakemake**:
   - Verifique o diretório `.snakemake/log` para quaisquer logs de erro.
   - Certifique-se de que o `Snakefile` está configurado corretamente com as regras `install_dependencies` e `run_flask`.

4. **Problemas na Instalação de Dependências**:
   - Certifique-se de que todos os pacotes necessários estão listados no arquivo `requirements.txt`.
   - Verifique se as versões corretas dos pacotes estão instaladas.

5. **Falhas nas Requisições de API**:
   - Verifique a conexão de rede e certifique-se de que as APIs externas (dbSNP, ClinVar, Ensembl) estão acessíveis.
   - Verifique se os endpoints da API e os parâmetros de requisição estão configurados corretamente no arquivo `api_getters.py`.

6. **Problemas na Renderização de Templates HTML**:
   - Certifique-se de que os templates HTML no diretório `templates` estão configurados corretamente e referenciados no arquivo `views.py`.
   - Verifique se há erros de sintaxe ou variáveis ausentes nos templates.

Se o problema persistir, considere buscar ajuda da comunidade ou consultar a documentação oficial das respectivas ferramentas e bibliotecas usadas no projeto.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT). Consulte o arquivo LICENSE para mais informações.

## Contato

Madson Aragão\
[madsondeluna@gmail.com](mailto\:madsondeluna@gmail.com)\
[LinkedIn](https://www.linkedin.com/in/madsonaragao)

🌟 <i>Created by Madson Aragão in somewhere, where bytes and biomolecules collide.</i>

