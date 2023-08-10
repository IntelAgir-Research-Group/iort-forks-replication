# Replication Package - Extração de Forks de Repositórios de IoRT

Aqui você encontra os detalhes de implementação do nosso trabalho "Mineração de Repositórios de Software para Internet das Coisas e Robótica (IoRT): Análise Inicial dos Forks".
Nossa abordagem consiste em 3 etapas principais, conforme mostrado na figura abaixo.

<img src="./workflow.png" width="400px">

O trabalho tem como base uma lista de repositórios de software disponíveis [nessa](https://github.com/IntelAgir-Research-Group/sbcars2021-replication-package-mining-iot) outra publicação anterior.


## Banco de Dados (Dados Extraídos)
Este estudo foi realizado por membros do Grupo de Pesquisa Intel Agir, com o apoio da Fundação Araucária, com bolsa PIBIC, sob a orientação do professor Michel Albonico.

- [Michel Albonico](https://michelalbonico.github.io) (Professor da Universidade Tecnológica Federal do Paraná)
- [Alexandre Corneau](https://github.com/ALEXANDRECORNEAU) (Bolsista PIBIC da Universidade Tecnológica Federal do Paraná)

## Construindo o conjunto de dados
O procedimento de mineração dos repositórios de software foi automatizado utilizando scripts de Python e a API REST do GitHub. Neste repositório, disponibilizamos os códigos de Python utilizados. 

Nossos scripts são organizados da seguinte forma:

````
./--- buscador/                 Pasta aonde fica o código de mineração dos repositórios do GitHub.
    |--- Buscador.py            Código que realiza a busca dos repositórios de usuários do GitHub que fizeram fork.
    |--- requirements.txt       Dependências do Python. Digitar "pip install -r requirements.txt".
    |--- keywords               Lista de usuários do GitHub com seus repositórios, usado pelo `Buscador.py`.
    |--- config.json            Script para informar as configurações do GitHub API, incluindo as credencias de acesso.
````

1. Inicialmente, são mineradas as informações principais de todos os forks dos repositórios listados no trabalho anterior. Para isso,
```python
$ bla bla
```
   
2. A partir dos fork, inciamos a mineração dos seus donos (usuários do GitHub).
   
```python
$ python3 Buscador.py
```
