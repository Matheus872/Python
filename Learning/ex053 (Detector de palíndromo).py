frase = str(input('Insira uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] #IMPORTANTE
l = len(junto)
print(inverso)
if inverso == junto:
    print('É um palíndromo!')
else:
    print('NÃO é um palíndomo!')