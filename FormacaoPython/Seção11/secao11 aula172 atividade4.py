with open('exercicio4.txt', 'wt') as arquivo:
    for i in range(0, 101):
        if i < 100 and i % 3 == 0:
            arquivo.write(f'{str(i)}\n')
