import calendar
a = int(input('Entre com o ano: '))
ab6 = calendar.isleap(a)
if ab6 is True:
    print('O ano é bissexto!')
else:
    print('O ano NÃO é bissexto!')


'''
    if a == 0:
        a = datetime
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print('O ano é bissexto!')
    else:
        print('O ano NÃO é bissexto!')
'''