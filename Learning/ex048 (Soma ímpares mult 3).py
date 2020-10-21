s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
     s = s + i
print(f'A soma dos ímpares multiplos de 3 entre 1 e 500 é: {s}')