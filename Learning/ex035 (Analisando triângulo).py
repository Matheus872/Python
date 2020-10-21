r1 = float(input('Insir o tamanho da reta 1: '))
r2 = float(input('Insira o tamanho da reta 2: '))
r3 = float(input('Insira o tamanho da reta 3: '))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('é possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
