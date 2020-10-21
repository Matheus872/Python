s = 0
for i in range(1, 7, 1):
    n = int(input(f'Insira o {i}º número: '))
    if i % 2 == 0:
        s = n + i
print(f'A soma dos números pares entre os 6 números passados é: {s}')