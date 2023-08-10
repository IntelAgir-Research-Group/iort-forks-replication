import requests
import csv
import json

# Ler o token de acesso pessoal do arquivo config.json
def ler_token():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config.get('token', '')

# Ler a lista de repositórios do arquivo TXT
def ler_repositorios(file_path):
    with open(file_path, 'r') as file:
        repositorios = [linha.strip() for linha in file.readlines()]
    return repositorios

# Obter informações dos forks de um repositório usando a API do GitHub
def obter_forks(repo):
    GITHUB_TOKEN = ler_token()

    if not GITHUB_TOKEN:
        print('Token de acesso não encontrado no arquivo config.json.')
        return

    url = f'https://api.github.com/repos/{repo}/forks'
    headers = {'Authorization': f'Token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
   
    if response.status_code == 404:
        print(f'Repositório não encontrado: {repo}')
        return []

    response.raise_for_status()
   
    return response.json()

# Salvar informações dos forks em um arquivo CSV
def salvar_csv(dados, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Repositório Original', 'Nome do Fork', 'Owner do Fork', 'URL do Owner', 'Link do Fork'])
        for item in dados:
            if not item:  # Ignorar itens vazios (quando não há forks)
                continue
                
            owner_login = item['owner']['login']
            owner_url = item['owner']['html_url']
            writer.writerow([item['name'], item['full_name'], owner_login, owner_url, item['html_url']])

def main():
    input_file = 'lista_repositorios.txt'
    output_file = 'forks.csv'

    repositorios = ler_repositorios(input_file)

    dados_forks = []

    for repo in repositorios:
        forks = obter_forks(repo)
        dados_forks.extend(forks)

    salvar_csv(dados_forks, output_file)
    print('Informações dos forks salvas em', output_file)

if __name__ == '__main__':
    main()
