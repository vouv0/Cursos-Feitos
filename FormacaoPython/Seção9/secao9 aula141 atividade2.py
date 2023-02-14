def acessa_lista(lista, indice):
    try:
       return f'Elemento da lista: {lista[indice]} no indíce {indice}'
    except IndexError:
        return None


lista1 = [1, 2, 3, 4, 5]
print(acessa_lista(lista1, 2))
