cod, qnt = map(float, input().split())

if (cod == 1):
  x = (qnt*4)
  print("Total: R$ {:.2f}".format(x))
elif (cod == 2):
  x = (qnt*4.5)
  print("Total: R$ {:.2f}".format(x))
elif (cod == 3):
  x = (qnt*5)
  print("Total: R$ {:.2f}".format(x))
elif (cod == 4):
  x = (qnt*2)
  print("Total: R$ {:.2f}".format(x))
else:
  x = (qnt * 1.5)
  print("Total: R$ {:.2f}".format(x))
