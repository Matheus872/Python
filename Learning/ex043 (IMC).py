h = float(input('Insira a sua altura em metros: '))
p = float(input('Insira o seu peso em quilos: '))
imc = (p)/(h*h)
print(f'O seu IMC é de : {imc}')
if imc <= 18.5 :
    print('Você está abaixo do peso!')
elif imc > 18.5 and imc <= 20:
    print('Seu peso é ideal!')
elif imc > 20 and imc <= 30:
    print('Você está com sobrepeso!')
elif imc > 30 and imc <= 40 :
    print('Você está obeso!')
else:
    print('Você está com obesidade mórbida!')
