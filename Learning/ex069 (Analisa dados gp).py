maiores = novinhas = homens = i = 0
sexo = op = ''
while True:
    i = int(input('Insira a idade da pessoa: '))
    sexo = str(input('Insira o sexo da pessoa [H/M]: ')).upper().strip()
    while sexo not in 'hHmM':
        sexo = str(input('Insira o sexo da pessoa [H/M]: ')).upper().strip()
    print('-'*30)
    if sexo == 'H':
        homens = homens + 1
    if  i > 18:
        maiores = maiores + 1
    if sexo == 'M' and i < 20:
        novinhas = novinhas + 1
    op = str(input('Deseja inserir mais alguma pessoa [S/N]: ')).upper().strip()
    while op not in 'sSnN':
        op = str(input('Deseja inserir mais alguma pessoa [S/N]: ')).upper().strip()
    if op == 'N':
        break
print('=-'*30)
print(f'Nesse grupo de pessoas há:\n{maiores} maiores de idade;\n{homens} homens e,\n{novinhas} novinhas dlç ai ui vem papai')