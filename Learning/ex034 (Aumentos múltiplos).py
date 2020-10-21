s = float(input('Insira o salário atual: '))
if s>1250:
    sa = 1.1*s
else:
    sa = 1.15*s
print('O salário com aumento é de:  R${:.2f}'.format(sa))