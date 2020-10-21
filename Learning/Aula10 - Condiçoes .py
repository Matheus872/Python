tempo = int(input("Insira o tempo de uso do seu carro: "))
preço = int(input('Insira o valor do carro: '))
if tempo<=3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('Caro' if preço>1000 else 'Barato!') #Pode ser simplificado dessa forma