import re

texto = 'Eu estou sorrindo, comendo e viajando agora.'

info = re.findall("[\w]+indo+|[\w]+ando+|[\w]+endo+", texto)

if info != None:
    print(f'"{texto.capitalize()}" contem um gerúndio.')
    print(f'Encontrado em: {info}')

else:
    print(f'{texto.capitalize()} não é um gerúndio.')
