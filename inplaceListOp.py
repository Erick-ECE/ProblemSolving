## lists operations in-pace

#reverse:
def rev(l):
    for i in range(len(l)//2):
        aux= l[i]
        l[i]= l[-(i+1)]
        l[-(i+1)]= aux


#left rotation
def leftRot(l,k):
    for i in range(k):
        first=l[0]
        for j in range(len(l)-1):
            l[j]=l[j+1]
        l[len(l)-1]=first

lista= [0,1,2,3,4,5,6,7,8,9]
k=12
leftRot(lista,k)

#rigth rotation
def rightRot(l,k):
    for i in range(k):
        last=l[len(lista)-1]
        for j in range(len(l)-1,-1,-1):
            l[j]=l[j-1]
        l[0]=last

rightRot(lista,k)