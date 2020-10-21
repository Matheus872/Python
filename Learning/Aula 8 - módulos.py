'''
import math (Importa a biblioteca inteira)  
from math import sqrt Importa uma única função da biblioteca


Funções da bilbioteca math
ceil - Arredondar para cima
floor - Arredondar para baixo
trunc - truncar número (Eliminar casas decimais)
pow - Potenciação
sqrt - Raiz quadrada
factorial - calcular fatorial

'''

from math import sqrt
from math import floor as redondabaixo #É possível dar um apelido aos métodos usando o "as"
num = int(input('Insira um número: '))
raiz = redondabaixo(sqrt(num))  #Caso importasse a biblioteca toda deveria usar math.sqrt()
print(f'A raiz de {num} é: {raiz}')