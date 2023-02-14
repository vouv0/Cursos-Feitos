from random import randrange

num = randrange(2, 100)

if num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é impar!')
