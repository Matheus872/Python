s = ''
#while s != 'M' and s!= 'H':
print('='*50)

s = str(input('Insira o seu sexo: ')).upper().strip()
while s not in 'MmFf':
    s = str(input('Dados inválidos. Por favor informe o seu sexo: ')).strip().upper()
print(f'Sexo {s} refistrado com sucesso!')
