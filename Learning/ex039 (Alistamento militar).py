i = int(input('Insira sua idade: '))
if i < 18:
    a = 18-i
    if a > 1:
        print(f'Ainda não é a hora de se alistar! Faltam {a} anos!')
    else:
        print(f'Ainda não é a hora de se alistar! Faltam {a} ano!')
elif i == 18:
    print('Está na hora de se alistar!')
else:
    a = i - 18
    if a > 1:
        print(f'Já passou da hora de se alistar! Atrasou {a} anos!')
    else:
        print(f'Já passou da hora de se alistar! Atrasou {a} ano!')