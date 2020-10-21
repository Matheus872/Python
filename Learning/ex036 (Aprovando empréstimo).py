v = float(input('Insira o valor da casa: '))
s = float(input('Insira o seu salário atual: '))
t = int(input('Em quantos anos pretende pagar a casa: '))
p = v/(t*12)
print('O valor da parcela é de {:.2f}'.format(p))
if p > 0.3*s:
    print('Empréstimo recusado!')
else:
    print('Empréstimo aprovado!')