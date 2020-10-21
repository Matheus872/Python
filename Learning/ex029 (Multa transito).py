v = int(input('Insira a velocidade do veículo: '))
if v>80:
    print(f'Você foi multado em R${(v-80)*7},00 reais')
else:
    print('Você não foi multado ...')