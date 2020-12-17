#sum of even fibonacci numbers till 4M
def fibo(n):
    n1=0
    n2=1
    c=0
    count=0
    suma=0
    while n>count:
        c = n1+n2
        #if c%2==0:
        #    print(c)
        n1=n2
        n2=c
        count+=1
        if c%2==0:
            suma+=c
    return(suma)

