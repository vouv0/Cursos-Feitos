def meses():
    yield 'Janeiro'
    yield 'Fevereiro'
    yield 'Março'
    yield 'Abril'
    yield 'Maio'
    yield 'Junho'
    yield 'Julho'
    yield 'Agosto'
    yield 'Setembro'
    yield 'Outubro'
    yield 'Novembro'
    yield 'Dezembro'


#for i,v in enumerate(meses()):
#    print(f'{i+1} - {v}')

mes = ' - '.join([str(v) for v in meses()])
print(mes)

