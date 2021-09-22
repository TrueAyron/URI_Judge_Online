entradas = int(input())
sapos = 0
ratos = 0
coelhos = 0

for i in range(entradas):
    x = input().split()
    if x[1] == 'S':
        sapos += int(x[0])
    elif x[1] == 'C':
        coelhos += int(x[0])
    elif x[1] == 'R':
        ratos += int(x[0])

t = sapos + coelhos + ratos

print(f"Total: {t} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print("Percentual de coelhos: {:.2f} %".format((coelhos / t) * 100))
print("Percentual de ratos: {:.2f} %".format((ratos / t) * 100))
print("Percentual de sapos: {:.2f} %".format((sapos / t) * 100))