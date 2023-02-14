def esta_na_lista_v2(lista, item):
    if item in lista:
        print(f'O valor foi encontrado, na posição {lista.index(item)}.')
    else:
        print('O valor não foi encontrado.')


n = [1, 2, 3, 'ola']
esta_na_lista_v2(n, 'ola')
