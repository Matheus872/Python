from time import sleep
n = int(input('Insira um número: '))
op = int(input('Escolha a base para conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n_'))
print('Processando...')
sleep(2)
if op == 1:
    print(f'O número em binário é : {bin(n)[2:]}')
elif op == 2:
    print(f'O número em octal é {oct(n)[2:]}')
elif op == 3:
    print(f'O número em hexadecimal é {hex(n)[2:]}')
else:
    print('Opção inválida!')
    exit()