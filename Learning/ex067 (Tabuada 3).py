n = 0
while True:
    n = int(input('Tabuada de qual número? '))
    if n < 0:
        break
    print('-'*30)
    for i in range(0, 11, 1):
        print(f'{i} x {n} = {i*n}')
    print('-'*30)

