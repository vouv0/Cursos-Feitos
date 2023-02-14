#DataFrame com dicionários
import pandas as pd

dados = {
    #'Nome': ['Ana', 'João', 'Maria', 'Vitor'],
    'Idade': [24,32,27,28],
    'Profissão': ['Engenheira', 'Dev', 'Médica', 'Analista']
}

data_frame = pd.DataFrame(dados, index=['Ana', 'João', 'Maria', 'Vitor'])
print(data_frame)
print('\n')
print(data_frame.loc['Maria']) #para localizar algo no DataFrame
