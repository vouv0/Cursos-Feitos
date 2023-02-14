def conta_letra_v2(txt, letra):
    lista = []
    for i, l in enumerate(txt):
        if l == letra:
            lista.append(i)
            continue
    return lista


print(conta_letra_v2('eita marieta', 'a'))
