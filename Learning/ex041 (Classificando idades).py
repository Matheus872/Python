i = int(input('Insira a sua idade: '))
if i < 0:
    print('Insira uma idade válida!')
    exit()
if i <= 9:
    print('A sua categoria é a \033[1:34mMIRIM')
elif i > 9 and i <= 14:
    print('A sua categoria é a \033[1:34mINFANTIL')
elif i > 14 and i <= 19:
    print('A sua categoria é a \033[1:34mJUVENIL')
elif i > 19 and i <=20:
    print('A sua categoria é a \033[1:34mSÊNIOR')
else:
    print('A sua categoria é a \033[1:34mMASTER')