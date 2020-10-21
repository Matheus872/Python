n = cont = soma = 0

while True:
    n = int(input('Insira um número: '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'Você inseriu {cont} números, e a soma entre eles é: {soma}')