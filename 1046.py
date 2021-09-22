a, b = map(int, input().split())

if (a > b):
    print("O JOGO DUROU {} HORA(S)".format(24 - (a - b)))
elif(b > a):
    print("O JOGO DUROU {} HORA(S)".format(b - a))
else:
    print('O JOGO DUROU 24 HORA(S)')