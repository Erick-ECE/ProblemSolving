#Write a function that returns the cumulative sum of elements in a list
def cumulativeSum(l):
    c = 0
    for i in range(len(l)):
        c+=l[i]
        l[i]=c
    return l

lista=[1,1,1]
cumulativeSum(lista)