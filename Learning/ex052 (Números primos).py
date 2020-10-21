n = int(input('Insira um número: '))
b = True
for i in range(2, n, 1):
    if n % i == 0:
        b = False
if b == True:
    print('O número é primo!')
else:
    print('O número NÃO é primo!')
