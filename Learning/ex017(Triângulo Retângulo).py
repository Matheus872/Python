from math import hypot

co = float(input('Tamanho do cateto oposto: '))
ca = float(input('Tamanho do catedo adjascente: '))
print(f'A hipotenusa vai medir {(co**2+ca**2)**(1/2)}')
print(f'A hipotenusa vai medir {hypot(co, ca)}')