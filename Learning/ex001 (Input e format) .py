nome = input('Qual é o seu nome ?   ')
print('É um grande prazer te conhecer {}!'.format(nome)) #Também pode ser feito com f'{}'
print('É um prazer te conhecer {:20}!'.format(nome)) #Formata a variável em 20 caracteres
print('É um prazer te conhecer {:>20}!'.format(nome)) #Pode usar > e < para alinhar à direita ou esquerda
print('É um prazer te conhecer {:^20}!'.format(nome)) #Meio
print('É um prazer te conhecer {:=^20}!'.format(nome)) #Centralidado entre iguais
# Para não quebrar a linha pode usar um , end= ''

print('Linha 1', end= ' ')
print('Linha 2')

# \n Para quebrar as linhas
print('Quebra \nlinha')