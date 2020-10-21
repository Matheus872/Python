from random import randint
from emoji import emojize
r = n = s = c = 0
op = ''
while True:
    print('-'*30)
    op = str(input('Par ou ímpar ? ')).upper().strip()
    n = int(input('Insira um número: '))
    print('-' * 30)
    r = randint(0, 10)
    print('=' * 30)
    print(f'SOMA = {s + n}')
    if op == 'PAR':
        s = r + n
        if (s + n) % 2 == 0:
            print(f'Parabéns, você venceu!\nO computador mostrou {r}')
            c = c + 1
            print('=' * 30)
        else:
            print(emojize(f'Infelizmente você perdeu :sweat:\nO computador mostrou {r}\nSequência de vitórias: {c}', use_aliases=True))
            print('=' * 30)
            break
    elif op == 'IMPAR':
        if (s + n) % 2 != 0:
           print(f'Parabéns, você venceu!\nO computador mostrou {r}')
           c = c + 1
           print('=' * 30)
        else:
            print(emojize(f'Infelizmente você perdeu :sweat:\nO computador mostrou {r}\nSequência de vitórias: {c}', use_aliases=True))
            print('=' * 30)
            break