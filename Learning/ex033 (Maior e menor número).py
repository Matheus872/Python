a = int(input('Insira um valor: '))
b = int(input('Insira um valor: '))
c = int(input('Insira um valor: '))
menor = a
maior = b
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c
print(f'O maior valor é: {maior}\nO menor valor é: {menor}')