dias_mes = []
for x in range(1, 32):
    dias_mes.append(x)

dia = int(input('Insira  dia que você nasceu: '))
dias_mes.remove(dia)

print(dias_mes)
