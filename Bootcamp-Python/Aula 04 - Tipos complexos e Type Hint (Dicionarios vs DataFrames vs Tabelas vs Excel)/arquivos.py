import csv

path: str = "/Users/renanmarx/Documents/Projetos/Estudos-Engenharia-de-Dados/Bootcamp-Python/Aula 04/exemplo.csv"

arquivo_csv: list = []

with open(file = path, mode = 'r', encoding = 'utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)