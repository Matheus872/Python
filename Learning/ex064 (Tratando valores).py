s = 0
cont = 0
n = 0
n = int(input('Insira um número: '))
while n != 999:
    cont += 1
    s = s + n
    n = int(input('Insira um número: '))
print(f'{cont} números foram inseridos, a soma deles é {s}')