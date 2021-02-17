# remove duplicates from a sorted array inplace

def removeDup(l):
        for i in l:
            c = l.count(i)
            if c>1:
                for j in range(c-1):
                    l.remove(i)
        return len(l)


lista= [1,1,1,2,2,3,3,3,3,4,5,5,6,6,6,6,6,7]

print(len(lista))
print(removeDup(lista))
print(lista)

# option 2
def delDup(l):
    j=0
    while j<(len(l)-1):
        if l[j]== l[j+1]:
            del(l[j])
        else:
            j=j+1
    return j+1
lista=[1,1,2]
print(delDup(lista))   
