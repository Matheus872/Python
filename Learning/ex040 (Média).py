n1 = float(input('Insira a sua nota 1: '))
n2 = float(input('Insira a sua nora 2: '))
m = (n1+n2)/2
if m < 5:
    print('Infelizmente você foi reprovado!')
elif m > 5 and m < 6.9:
    print('Você está de recuperação, estude mais!')
else:
    print('Parabéns, você foi aprovado!')