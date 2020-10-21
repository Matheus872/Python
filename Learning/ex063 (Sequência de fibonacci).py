q = int(input('Quantos termos deseja mostrar? '))
c = 0
t1 = 0
t2 = 1
t3 = 0
while c != q:
    t3 = t1 + t2
    if c == 0:
        print('0 -> ', end= '')
    elif c == 1:
        print('1 -> ', end= '')
    else:
        print(f'{t3} -> ', end= '')
        t1 = t2
        t2 = t3
    c = c + 1
print('FIM')
