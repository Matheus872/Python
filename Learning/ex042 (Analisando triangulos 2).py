r1 = float(input('Insir o tamanho da reta 1: '))
r2 = float(input('Insira o tamanho da reta 2: '))
r3 = float(input('Insira o tamanho da reta 3: '))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('É possível formar um triângulo!')
    if r1 == r2 and r2 == r3:
        print('O triângulo a ser formado será \033[1:31mEQUILÁTERO\033[m!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo a ser formado será \033[1:31mISÓCELES\033[m!')
    else:
        print('O triângulo a ser formado será \033[1:31mESCALENO\033[m!')
else:
    print('Não é possível formar um triângulo!')
