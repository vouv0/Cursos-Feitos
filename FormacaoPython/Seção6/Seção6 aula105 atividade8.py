def limpa_chat(lista, txt=''):
    for palavra in txt.split():
        if palavra in lista:
            txt = txt.replace(palavra,'*')
    return txt


lista1 = ['puts', 'eita', 'ola']
txt1 = input('Insira um texto: ')

print(limpa_chat(lista1, txt1))
