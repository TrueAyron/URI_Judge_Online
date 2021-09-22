N = float(input())
print("NOTAS:")
cs=[100,50,20,10,5,2]

for c in cs:
  qtd_cs = int(N/c)
  print("{} nota(s) de R$ {:.2f}".format(qtd_cs,c))
  N-= qtd_cs*c

print("MOEDAS:")
ms=[1,0.50,0.25,0.10,0.05,0.01]

for m in ms:
  qtd_ms=int(round(N,2)/m)
  print("{} moeda(s) de R$ {:.2f}".format(qtd_ms,m))
  N-= qtd_ms*m