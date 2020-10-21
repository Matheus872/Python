c = 0
for i in range(1, 8, 1):
    i = int(input(f'Insira a {i}º idade: '))
    if i >= 18:
        c = c + 1
print(f'Totalizando {c} pessoas maiores de idade!')