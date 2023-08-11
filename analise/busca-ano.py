import csv
import requests
import json

def get_config():
    with open('../buscador/config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

def get_repo_info(url, headers):
    print(f'https://api.github.com/repos/{url}')
    response = requests.get(f'https://api.github.com/repos/{url}', headers=headers)
    data = response.json()
    created_date = data.get('created_at')  # Usando .get() para evitar KeyError
    updated_date = data.get('updated_at')  # Usando .get() para evitar KeyError
    return created_date, updated_date

config = get_config()
github_token = config['token']

headers = {
    'Authorization': f'Bearer {github_token}'
}

with open('csv/forks_year.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Pule o cabeçalho do CSV

    updated_rows = []
    for row in csv_reader:
        fork_url = row[0]
        created_date, updated_date = get_repo_info(fork_url, headers)
        row[1] = created_date
        row[2] = updated_date
        updated_rows.append(row)

with open('csv/forks_year_atualizado.csv', 'w', newline='') as updated_csv_file:
    csv_writer = csv.writer(updated_csv_file)
    csv_writer.writerow(['fork_url', 'created', 'updated'])  # Escreva o cabeçalho
    csv_writer.writerows(updated_rows)  # Escreva as linhas atualizadas
