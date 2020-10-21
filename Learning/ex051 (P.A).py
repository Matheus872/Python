a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
an = 0
print(f'Os 10 primeiros termos da PA são: ')
for i in range(1, 11, 1):
     an = a1 + (i-1)*r
     print(f'{an}')