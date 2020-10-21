s = '='*50
print (f'{s}')
num = float(input('Digite um número: '))  # O int antes do input é chamado de tipo primitivo, transforma o parâmetro em inteiro
num2 = float(input('Digite outro número: '))
print(f'A soma entre {num} e {num2} é igual a {num + num2}!')  # o f antes das aspas serve para formatar, também pode ser feito como | print('A soma entre {} e {} é igual a {}!'.format(num,num2,num+num2))
print('a divisão entre {} e {} é igual a {:.3f}'.format(num, num2, num/num2)) #O :.3f faz com que mostre 3 casas decimais

'''
** Potência - Também pode ser feita com 'pow(4,3)' = (4^3)
// Divisão inteira
% Resto de divisão

'''