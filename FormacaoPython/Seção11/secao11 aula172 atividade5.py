import csv


def escreve_csv(nome, parentesco):
    with open('exercicio5.csv', 'a') as arquivo:
        escritorCsv = csv.writer(arquivo, delimiter=',')
        escritorCsv.writerow(['Nome', 'Parentesco'])
        escritorCsv.writerow([nome, parentesco])


def le_csv(file):
    with open(file, 'r') as arquivo:
        print(arquivo.read())



pessoa1 = escreve_csv('Vitor', 'Filho')
pessoa2 = escreve_csv('Angela', 'Mãe')
pessoa3 = escreve_csv('Hilario', 'Irmão')
pessoa4 = escreve_csv('Paula', 'Irmã')
pessoa5 = escreve_csv('Theo', 'Sobrinho')


le_csv('exercicio5.csv')
