biggus = 0
ind = 0

for i in range (100) :
    num = int(input())
    if biggus < num :
        biggus = num
        ind = i+1
        
print(biggus)
print(ind)