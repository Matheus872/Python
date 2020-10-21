n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
op = 0
while op != 5:
    op = int(input("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] SAIR
_"""))
    if op == 2:
     print(f'O produto entre {n1} e {n2} é: {n1*n2}')
    elif op == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif op == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior número é {n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2}, o maior número é {n2}')
        else:
            print('Não existe número maior! Os dois números são iguais!')
    elif op == 4:
        n1 = int(input('Insira um número: '))
        n2 = int(input('Insira outro número: '))
    elif  op > 5 or op < 1:
        print('Insira uma opção válida!')