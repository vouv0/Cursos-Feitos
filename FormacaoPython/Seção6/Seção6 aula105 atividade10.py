def inteiro(lista):
    lista2 = []
    for item in lista:
        if item.isdecimal():
            item = int(item)
            lista2.append(item)
    return sorted(lista2)


ls = ['um', 'dois', '1', '1.23', '33', '2', '7', '4']

print(inteiro(ls))
