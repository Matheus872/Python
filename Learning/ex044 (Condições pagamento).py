print('{:=^40}'.format(' Lojas Mathios '))
v = float(input('Insira o valor do produto: '))
op = int(input('Escolha uma condição de pagamento: \n1 - À vista\n2 - Débito\n3 - Crédito até 2x\n4 - Crétido 3x ou mais\n_'))
if op == 1:
    p = v*0.9
elif op == 2:
    p = v*0.95
elif op == 3:
    p = v
elif op == 4:
    p = v*1.2
else:
    print('Insira uma opção válida!')
    exit()
print('Opção escolhida: {}\nO valor normal do produto é de R${:.2f}\nO valor do produto com a condição de pagamento escolhida é de R${:.2f}'.format(op, v, p))