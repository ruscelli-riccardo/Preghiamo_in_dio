def confronto():
    x=int(input('numero uno: '))
    y=int(input('numero due: '))
    z=int(input('numero tre: '))
    if x > y and x > z :
        print(x)
    elif y > x and y > z : 
        print(y)
    else: print(z)
confronto()