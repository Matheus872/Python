n = op = barato = ''
p = t = mil = b = 0
while True:
    n = str(input('Insira o nome do produto: '))
    p = float(input('Insira o preço do produto: '))
    if b == 0:
        b = p
    if p <= b:
        b = p
        barato = n
    op = str(input('Você deseja inserir mais slgum produto ? [S/N] ')).upper().strip()
    t = t + p
    if p > 1000:
        mil = mil + 1
    while op not in 'sSnN':
        op = str(input('Resposta inválida.\nVocê deseja inserir mais slgum produto ? [S/N] ')).upper().strip()
    if op == 'N':
        break

print('=-'*30)
print('O valor total da compra é: R$ {:.2f};\n{} produtos custam mais de R$ 1000,00 e,\nO produto mais barato é: {}'.format(t, mil, barato))
