string = input('Entre com um valor: ')             # O método .is[...] verifica informações sobre uma variável e retorna um booleano
print(type(string))    # O type retorna a classe da variável
print(f'É alfabético ?  {string.isalpha()}')
print(f'É numérico ?  {string.isnumeric()}')
print(f'É maiúsculo ?  {string.isupper()}')
