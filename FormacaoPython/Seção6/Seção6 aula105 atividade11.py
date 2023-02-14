from datetime import datetime

hoje = datetime.now()
data_nascimento = input('Insira Dia/Mes/Ano de nascimento: ')
nascimento = datetime.strptime(data_nascimento, f'%d/%m/%Y')

dias = hoje -nascimento

print(f'Você já viveu {dias.days} dias')
