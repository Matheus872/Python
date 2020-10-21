#Matheus Henrique 29/06/2020
#------------------------------------------------------------------------------------------------------------
from pygame import mixer            #Importando bibliotecas
import emoji
from time import sleep
from random import randint
#------------------------------------------------------------------------------------------------------------
mixer.init()                            #Colocando música - Copie uma música e cole na pasta do projeto aqui
mixer.music.load('Falling.mp3')         #no pycharm, depois coloque o nome dela entre os '' nessa linha <--
mixer.music.play()                      #lembre-se de por o formato ex: mixer.music.load('NOMEDOARQUIVO.mp3')
#-------------------------------------------------------------------------------------------------------------
print(emoji.emojize('EU DUVIDO QUE HUMANOS POSSAM VENCER AS MÁQUINAS NO JOKENPÔ! :smiling_imp:', use_aliases=True))
print("**"*30)
op = int(input(emoji.emojize('Pedra papel ou tesoura ?\n1 - Pedra :punch:\n2 - Papel :hand:\n3 - Tesoura :v:\n_',use_aliases=True)))
print('**'*30)
if op > 3 or op < 1:
    print(emoji.emojize('O QUE FOI ? ESTÁ FUGINDO ???  :smiling_imp:\n\n(Selecione uma opção válida)', use_aliases=True))
    exit()
pc = randint(1,3)
print('Jooo..')
sleep(1)                                                     #Entrando com a opção do jogador ...
print('Keenn..')
sleep(1)
print('PÔ')
sleep(1)
#--------------------------------------------------------------------------------------------------------------
if pc == 1:
    if op == 1:                                             #Se o PC "escolheu" Pedra
        print("**" * 30)
        print(emoji.emojize(':punch: \033[1:33mVS\033[m :punch:\n\033[1:31m EMPATE\033[m!',use_aliases=True))
        print("**"*30)
    elif op == 2:
        print("**" * 30)
        print(emoji.emojize(':hand: \033[1:33mVS\033[m :punch:\n\033[1:32m Você Ganhou!!!\033[m', use_aliases=True))
        print("**" * 30)
    elif op == 3:
        print("**" * 30)
        print(emoji.emojize(':v: \033[1:33mVS\033[m :punch:\n\033[1:31mEu Ganhei!! HEHEHE\033[m!', use_aliases=True))
        print("**" * 30)
#-----------------------------------------------------------------------------------------------------------------
elif pc == 2:
    if op == 1:                                            #Se o PC "escolheu" Papel
        print("**" * 30)
        print(emoji.emojize(':punch: \033[1:33mVS\033[m :hand:\n\033[1:31mEu Ganhei!! HEHEHE\033[m!',use_aliases=True))
        print("**"*30)
    elif op == 2:
        print("**" * 30)
        print(emoji.emojize(':hand: \033[1:33mVS\033[m :hand:\n\033[1:31m EMPATE\033[m!', use_aliases=True))
        print("**" * 30)
    elif op == 3:
        print("**" * 30)
        print(emoji.emojize(':v: \033[1:33mVS\033[m :hand:\n\033[1:32m Você Ganhou!!!\033[m', use_aliases=True))
        print("**" * 30)
#---------------------------------------------------------------------------------------------------------------
elif pc == 3:
    if op == 1:                                            #Se o PC "escolheu" Tesoura
        print("**" * 30)
        print(emoji.emojize(':punch: \033[1:33mVS\033[m :v:\n\033[1:32m Você Ganhou!!!\033[m', use_aliases=True))
        print("**" * 30)
    elif op == 2:
        print("**" * 30)
        print(emoji.emojize(':hand: \033[1:33mVS\033[m :v:\n\033[1:31mEu Ganhei!! HEHEHE\033[m!', use_aliases=True))
        print("**" * 30)
    elif op == 3:
        print("**" * 30)
        print(emoji.emojize(':v: \033[1:33mVS\033[m :v:\n\033[1:31m EMPATE\033[m!', use_aliases=True))
        print("**" * 30)
