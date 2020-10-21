from pygame import mixer, event
mixer.init()
mixer.music.load('Falling.mp3')
mixer.music.play()
input('')


'''
Por alguma incompatibilidade com o sistema, quando o pygame é inicializado, 
ele requer mais coisas do que estamos dando. A alternativa mais fácil é utilizar
apenas o mixer e procurar outra forma de manter o programa funcionando,
como import time junto com time.sleep(x) ou apenas um input.
'''
