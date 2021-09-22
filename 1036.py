from math import sqrt

a, b, c = map(float, input().split())

d = (b ** 2) - (4 * a * c)

if (d < 0 or a == 0.0):
  print("Impossivel calcular")
else:
  r1 = (-b + sqrt(d)) / (2*a)
  r2 = (-b - sqrt(d)) / (2*a)
  print("R1 = {:.5f}".format(r1))
  print("R2 = {:.5f}".format(r2))