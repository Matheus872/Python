n = int(input('Insira um número: '))
c = n
r = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end= '')
    r = r * c
    c = c - 1
    print(' x ' if c >= 1 else ' = ', end= '')
print(f'{r}')