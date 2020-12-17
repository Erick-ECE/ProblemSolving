# busqueda Binaria recursiva
def bb(l,e): # bb(l:lista , e: elemento a bucar en l)
    l.sort()
    m= len(l)//2
    print(l,m)
    if not l : return False
    if l[m] == e:
        return True
    elif  l[m] < e:
        return bb(l[m + 1:],e)
    else:
        return bb(l[:m],e)
   

lista = [8,9,5,4,3,6,4,2,1,10]

print(bb(lista,1))


# busqued binaria iterativa

def bbi(l,e):
    l.sort()
    m= len(l)//2
    ini=0
    fin=len(l)-1
    while ini<=fin:
        #print(ini,fin,m)
        if l[m] == e: return m
        elif l[m] > e:
            fin = m-1
            m= ((fin-ini)//2) +ini
        elif l[m] < e:
            ini=m+1
            m= ((fin-ini)//2) + ini
    return False

print(bbi(lista,81))