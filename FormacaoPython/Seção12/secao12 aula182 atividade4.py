import re

texto = '95223344'

info = re.search('^([0-9]){8}$', texto)
info2 = re.search('^95',texto)

if info != None:
    print('É um número valido.')
    if info2:
        print('Número bloqueado.')
else:
    print('Não é um número válido.')
