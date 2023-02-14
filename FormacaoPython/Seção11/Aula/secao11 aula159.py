import csv


with open('pessoas.csv', 'w') as arquivo:
    escritorCsv = csv.writer(arquivo, delimiter=',')
    escritorCsv.writerow(['id', 'nome', 'profissão'])
    escritorCsv.writerow(['1', 'Vitor', 'Dev'])
    escritorCsv.writerow(['2', 'João', 'Professor'])
    escritorCsv.writerow(['3', 'Ana', 'Engenheira'])

