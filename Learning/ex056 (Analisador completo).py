cont = 0
idve = 0
nomeve = ''
soma = 0
m = 0
for i in range(1, 6, 1):
    n = str(input('Insira o seu nome: '))
    id = int(input('Insira a sua idade: '))
    s = str(input('Insira o seu sexo: '))
    print('='*20)
    if s == 'm':
        if id < 20:
            cont = cont + 1
    soma = soma + id
    if s == 'h':
        if id > idve:
            idve = id
            nomeve = n
m = soma/5
print(f'O Homem mais velho é: {nomeve}\nO número de uiui que dlç é: {cont}\nA média de idade do grupo é: {m}')