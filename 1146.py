while True:
    var = int(input())
    vaz = ''
    
    if var != 0:
        for i in range(1, var+1):
          vaz += str(i) + ' '
        print(vaz.strip())     

    else:
        break
