n = int(input())
x = False
num = []

while n <= 100 and n >= 0:
    for i in range(n):
        num.append(int(input()))
    break

for i in num:
    if i == 2 or i == 3 or i == 5:
        print(f"{i} eh primo")
    else:
        ehprimo = False
        for z in range(2, int(i / 2)):
            if (i % z) == 0:
                ehprimo = False
                break
            else:
                ehprimo = True
        if ehprimo:
            print(f'{i} eh primo')
        else:
            print(f'{i} nao eh primo')