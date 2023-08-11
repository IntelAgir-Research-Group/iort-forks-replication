import csv
import requests

def check_github_repo_availability(repo_url):
    response = requests.get(repo_url)
    print(response.status_code)
    if response.status_code == 200:
        return "sim"
    elif response.status_code == 404:
        return "nao"
    else:
        return "desconhecido"

# Nome do arquivo CSV a ser lido
csv_filename = "csv/forks_disponiveis.csv"

# Lista para armazenar os dados atualizados
updated_data = []

# Abre o arquivo CSV para leitura
with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    updated_data.append(headers)  # Adiciona o cabeçalho na lista atualizada

    for row in reader:
        repo_url = repo_url = "https://github.com/"+row["fork_repo"].strip()
        availability = check_github_repo_availability(repo_url)
        row["disponivel"] = availability
        updated_data.append(row)

# Escreve os dados atualizados de volta para o arquivo CSV
output_csv_filename = "csv/atualizado_" + csv_filename
with open(output_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()  # Escreve o cabeçalho no arquivo de saída
    writer.writerows(updated_data[1:])  # Escreve os dados, excluindo o cabeçalho repetido

print("Processo concluído. Arquivo atualizado foi salvo como 'atualizado_seuarquivo.csv'.")
