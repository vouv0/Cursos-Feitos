def soma(n1, n2):
    soma = n1 + n2
    soma = min(10000, soma)
    soma = max(0, soma)
    return soma


print(soma(5000,6000))
