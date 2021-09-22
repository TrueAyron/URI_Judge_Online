lista = []

while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0 :
        break
    if m < n:
        ax = m
        m = n
        n = ax

    sequencia = ''
    soma = 0

    for i in range(n, m + 1):
        sequencia += str(i) + " "
        soma += i

    lista.append(f"{sequencia}Sum={soma}")

for i in lista:
    print(i)