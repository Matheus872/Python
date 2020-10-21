d = float(input('Qual a distância da viagem em Km ? '))
if d<=200:
    v = d*0.5
else:
    v = d*0.45
print('O valor da passagem é R${:.2f}'.format(v))