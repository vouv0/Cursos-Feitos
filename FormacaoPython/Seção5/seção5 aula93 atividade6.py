def esta_na_lista(lista, param):
    if param in lista:
        return True
    return False


n = [1, 2, 3]
print(esta_na_lista(n, 1))
