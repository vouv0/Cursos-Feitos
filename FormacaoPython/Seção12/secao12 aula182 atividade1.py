import re

dado = '37'

teste = re.search("^([2][0-9])|([3][0-5])$", dado)

if teste != None:
    print('Número válido')
else:
    print('Número inválido')
