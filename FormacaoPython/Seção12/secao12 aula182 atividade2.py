import re

texto = 'Eu estudo python.'

info = re.search('python', texto)

if info != None:
    print(f'Palavra encontrada: {info.span()}')
else:
    print('Palavra não encontrada.')
