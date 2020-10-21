op = ''
cont = 0
soma = 0
maior = 0
menor = 0
while op != 'N':
    op = str(input('Quer inserir mais algun número ? [S/N]')).upper()
    if op == 'S':
        n = int(input('Insira um número: '))
        cont = cont + 1
        soma = soma + n
        if cont == 1:
            maior = n
            menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'O maior número é: {maior}\nO menor número: {menor}\nMédia dos números: {soma/cont}')