import pytest


def test_nome_abreviatura(nome):
    div_nome = str(nome).upper().split()
    print(f'Seu nome inteiro é {nome}.')
    print(f'A abreviatura do seu nome é {div_nome[0][0]}{div_nome[-1][0]}.')


test_nome_abreviatura('Vitor Vouvouloudas de Moraes')
