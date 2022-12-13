lista=[]
x=int(input('quanti frutti: '))
for n in range(x):
    y=str(input('inserire frutto: '))
    lista.append(y)
lista.sort()
print(lista)