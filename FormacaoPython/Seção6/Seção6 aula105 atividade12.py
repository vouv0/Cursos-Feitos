from datetime import datetime

hoje = datetime.now()
data_aniversario = input('Insira Dia/Mes/Ano do seu proximo aniversário: ')
aniversario = datetime.strptime(data_aniversario, f'%d/%m/%Y')

dias = aniversario - hoje

print(f'Você fará aniversário daqui a {dias.days} dias.')
