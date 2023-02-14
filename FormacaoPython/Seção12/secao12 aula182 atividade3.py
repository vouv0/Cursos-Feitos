import re

texto = 'Segunda-Feira'

info = re.search('^(Segunda-Feira|Terça-Feira|Quarta-Feira|Quinta-Feira|Sexta-Feira|Sábado|Domingo|)$', texto)

if info != None:
    print('É um dia da semana.')
else:
    print('Não é um dia da semana.')
