# yield
l=[1,2,3,4,5,6,7,8,9,10]

def printItems(s):
    tam = len(s)
    cont = 0
    while tam:
        yield s[cont]
        cont+=1
        tam-=1

print(list(printItems(l)))