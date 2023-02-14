def citacao(func):
    def func_inner(txt):
        return f'"{func(txt)}"'.lower()
    return func_inner


@citacao
def transforma(txt):
    return txt


print('E disse João:', transforma('Só os sábios sabem!'))
