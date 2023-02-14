import re

texto = '23:30'

info = re.search("^([0-2][0-3]|[0-1][0-9])(:)([0-5][0-9])$", texto)

if info != None:
    print(f'Agora são {texto} hrs.')

else:
    print(f'{texto} não é um formato válido.')
