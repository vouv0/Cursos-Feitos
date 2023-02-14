import pytest


def test_nome(nome):
    div_nome = str(nome).capitalize().split()
    print(f'Seu nome inteiro é {nome}.')
    print(f'Primeiro nome {div_nome[0]} e último nome {div_nome[-1]}.')


test_nome('Vitor Vouvouloudas de Moraes')
