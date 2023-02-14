with open('exemplo_with.txt', 'wt') as arquivo:
    arquivo.write('Exemplo usando o "with".\n')
    arquivo.write('Dessa forma não é necessário fechar o arquivo.\n')
    arquivo.write('Ele fecha automaticamente quando sai da indentação.')
