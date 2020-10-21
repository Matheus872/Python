from random import randint
print('{:=^50}'.format(' Tente acertar o número que eu pensei! '))
n = 0
pc = randint(1, 10)
cont = 0
while n != pc:
    n = int(input('Insira um número de 1 a 10: '))
    if n > pc:
        print('Menos...', end= '')
    elif n < pc:
        print('Mais... ', end= '')
    cont = cont + 1
print(f'Paranéns, você acertou!\nPara isso você precisou de {cont} tentativas')
