maior = 0
menor = 0
for i in range(1, 6, 1):
    p = int(input(f'Insira o {i}º peso: '))
    if i == 1:
        menor = p
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print(f'O maior peso é: {maior}\nO menor peso é {menor}')