a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
an = 0
c = 0
print(f'Os 10 primeiros termos da PA são: ')
while c != 10:
     print(f'{an+a1} -> ', end= '')
     c = c + 1
     an = an + r
print('FIM')
p = c
t = 0
t = t + p
m = 1
while m != 0:
    m = int(input('Quantos termos você quer mostrar a mais? '))
    t = t + m
    while c != p + m:
        print(f'{an + a1} -> ', end='')
        c = c + 1
        an = an + r
    print('FIM')
    p = c
print(f'Foram mostrados {t} termos')
