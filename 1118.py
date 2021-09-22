while True:
    n = float(input())
    while n < 0 or n > 10:
        print('nota invalida')
        n = float(input())

    n2 = float(input())
    while n2 < 0 or n2 > 10:
        print('nota invalida')
        n2 = float(input())

    media = (n + n2) / 2
    
    print(f'media = {media:.2f}')

    novo = input('novo calculo (1-sim 2-nao)\n')

    while novo not in ['1', '2']:
        novo = input('novo calculo (1-sim 2-nao)\n')

    if novo == '2':
        break