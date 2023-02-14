def get_random_lista(inicial, final, tam=1):
    from random import randint
    lista_num = []
    for n in range(0, tam):
        num = randint(inicial, final)
        lista_num.append(num)
    return lista_num
