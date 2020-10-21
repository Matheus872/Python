import random
from time import sleep
n = [0, 1, 2, 3, 4, 5] #randint(0,5)
num = random.choice(n)
chute = int(input('Tente advinhar o número que escolhi: '))
print('Processando ...')
sleep(3)
if chute == num:
    print('Wow! Você acertou!')
else:
    print('Que pena ... Voê errou hehe!')