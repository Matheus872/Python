n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
if n1>n2:
    print(f'O número {n1} é maior que o número {n2}!')
elif n2>n1:
    print(f'O número {n2} é maior que o número {n1}!')
else:
    print('Não existe valor maior! Os dois números são iguais!')