#Reorganize String

def reorganize(s):
    d={}
    N=len(s)
    A=[]
    for i in s:
        d[i] = d.get(i,0)+1
    
    for i, j in sorted(d.items(), key=lambda item: item[1]):
        if j>((N+1)/2):
            return ''
        A.extend(i*j)
    result= [None]*N
    result[::2],result[1::2]=A[N//2:],A[:N//2]
    return ''.join(result)

s = "aab"
reorganize(s)
