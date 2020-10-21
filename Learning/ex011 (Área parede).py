l = float(input('Insira a largura da parede em metros: '))
h = float(input('Insira a altura da parede em metros: '))
a = l*h
print('='*60)
print(f'A parede tem {a} m²')
print('A parede precisa de {:.2f} litros de tinta para ser pintada'.format(a/2))
print('='*60)