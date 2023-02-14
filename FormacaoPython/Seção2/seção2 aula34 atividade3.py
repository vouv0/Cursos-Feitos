sinal_vermelho = False
carro_direita = True
carro_esquerda = True

atravessar_rua = sinal_vermelho or not carro_direita and not carro_esquerda
print(f'Posso atravessar a rua? {atravessar_rua}')