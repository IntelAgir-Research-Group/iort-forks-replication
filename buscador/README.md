# Mineração de Repositórios do GitHub

Antes de iniciar, insira seu token do GitHub no arquivo `config.json`.

Também não esqueça de instalar todas as dependências Python necessárias.

```python
$ pip install -r requirements.txt 
```
## Extração dos Forks

O primeiro passo é extrair todos os forks dos repositórios de software listados no [artigo anterior](https://github.com/IntelAgir-Research-Group/sbcars2021-replication-package-mining-iot).

```python
$ bla bla
```

## Busca Pelos Repositórios dos Usuários

Após todos os forks serem extraídos, buscamos informações relativas aos repositórios dos usuários donos dos forks. 

Todos os usuários são listados e ordenados pela quantidade de repositórios no arquivo `dev_qtde_repos-all-ordered.csv`.

**Isso pode demorar vários dias para executar.** Recomendamos dividir o arquivo dos usuários em vários e executar em partes.

```python
$ python3 busca-dev-repos.py
```
