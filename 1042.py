a, b, c = map(int, input().split())

if(a > b > c):
    print(c)
    print(b)
    print(a)
    print("")
    print(a)
    print(b)
    print(c)
elif(a > c > b):
    print(b)
    print(c)
    print(a)
    print("")
    print(a)
    print(b)
    print(c)
elif(b > a > c):
    print(c)
    print(a)
    print(b)
    print("")
    print(a)
    print(b)
    print(c)
elif(b > c > a):
    print(a)
    print(c)
    print(b)
    print("")
    print(a)
    print(b)
    print(c)
elif(c > a > b):
    print(b)
    print(a)
    print(c)
    print("")
    print(a)
    print(b)
    print(c)
else:
    print(a)
    print(b)
    print(c)
    print("")
    print(a)
    print(b)
    print(c)