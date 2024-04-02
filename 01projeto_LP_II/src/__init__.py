import csv
import os

print(os.getcwd())
try:
    with open('./database/movimentacoes.csv', 'x', newline='') as file:
        cabecalho = [['id', 'tipo', 'valor', 'ano', 'mes', 'dia']]
        escritor = csv.writer(file, delimiter=',')
        escritor.writerows(cabecalho)
except FileExistsError:
    pass

try:
    with open('./database/investimentos.csv', 'x', newline='') as file:
        cabecalho = [['id', 'tipo', 'capital', 'taxa', 'ano', 'mes', 'dia', 'montante', 'rendimento']]
        escritor = csv.writer(file, delimiter=',')
        escritor.writerows(cabecalho)
except FileExistsError:
    pass