frase = 'Curso em Vídeo Python'
print(frase[3]) # Fatiamento, pegando o caractere 3 (Começa do 0)
print(frase[3:13]) #Fatia do 3 até o 13-1
print(frase[:13]) #Fatia do começo até o 13-1
print(frase[6:]) #Fatia do 6 até o final
print(frase[0:15:2]) #Fatia do 0 ao 15-1, pulando de 2 em 2
print(frase[::2]) #Fatia do começo ao fim pulando de 2 em 2

print(""" texto
      muito
      grande
      """) #Com as 3 aspas podemos printar textos de diferentes linhas

print(frase.count('o')) #Conta quantas vezes tem 'o'
print(frase.count('o',0,13)) #Conta quantas vezes tem o 'o' do 0 ao 13-1
print(frase.find('deo')) #Retorna onde começa o 'deo'. Se a string passada como parâmetro não existir, será retornado -1
print(('Curso' in frase)) #Retorna verdadeiro se tiver 'Curso' na frase
print(frase.upper()) #Deixa tudo em maiúsculo
print(frase.lower()) #Deixa tudo em minísculo
print(frase.capitalize()) #Deixa tudo em minúsculo e upa a primeira
print(frase.title()) #Upa o que tiver depois dos espaços
print(len(frase)) #Retorna o número de carateres
print(frase.replace('Python', 'Android'))#Substitui o 1 pelo 2. Se faltar espaço ele é adicionado

frase2 = '   Aprenda Phyton  '
print(frase2.strip()) #Remove todos os espaços do começo e final da string
print(frase2.rstrip()) #Remove os espaços do final
print(frase2.lstrip()) #Remove os espaços do começo
print(frase.split()) #Gera uma lista com a frase fatiada onde tiver espaços
print(('-'.join(frase))) #Junta a string colocando '-' no lugar dos epaços