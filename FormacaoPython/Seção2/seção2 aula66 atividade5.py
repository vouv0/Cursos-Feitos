
for x in range(3, 31):
    primo = True
    for y in range(2, x):
        if x % y == 0:
            primo = False
            break
    if primo:
        print(f'O número {x} é primo.')
    else:
        print(f'O número {x} não é primo.')
