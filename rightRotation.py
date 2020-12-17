#right rotation

# return a copy
def rRotation(lista,k):
    return lista[(len(lista)-k)%len(lista):]+lista[:(len(lista)-k)%len(lista)]


#in place:
def rrot(l,k):
    for i in range(k):
        last=l[len(l)-1]
        for j in range(len(l)-1,-1,-1):
            l[j]=l[j-1]
        l[0]=last
   
l=[1,2,3,4,5,6,7]
k=10
rrot(l,k)
print(l)

# #in O(n)
# def rightRot(l,k):

