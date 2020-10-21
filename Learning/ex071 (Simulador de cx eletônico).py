v = int(input('Insira o valor que deseja sacar: '))
n50 = n20 = n10 = n1 = 0

while v - 50 >= 0:
    if v < 50:
        break
    v = v - 50
    n50 = n50 + 1
while v - 20 >= 0:
    if v < 20:
        break
    v = v - 20
    n20 = n20 + 1
while v - 10 >= 0:
    if v < 10:
        break
    v = v - 10
    n10 = n10 + 1
while v - 1 >= 0:
    if v < 1:
        break
    v = v - 1
    n1 = n1 + 1
print('=-'*30)
print(f'Notas de 50: {n50}\nNotas de 20: {n20}\nNotas de 10: {n10}\nNotas de 1: {n1}')