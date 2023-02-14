objetos = {'copo': 'beber', 'caneta': 'escrever', 'fone': 'ouvir'}

nome_obj = input('Insira o nome do objeto: ').lower()
if nome_obj not in objetos.keys():
    print('Objeto inválido, escolha entre: copo, caneta e fone.')
else:
    print(f'O objeto {nome_obj} tem função de {objetos[nome_obj]}.')
