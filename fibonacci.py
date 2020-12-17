# fibonacci
def fibo(n):
    if n == 0: return
    if n == 1: return 1
    s = 0
    n1=0
    n2=1
    count=0
    while n > count:
        print(s)
        s = n1+n2
        #print(s)
        n1=n2
        n2 = s
        count+=1

fibo(5)

# fibonacci recursivo

def fiboR(n):
    if n<=1: return n
    return (fiboR(n-1)+fiboR(n-2))

## geeksforgeeks
FibArray = [0,1]
 
def fibonacci(n):
    if n<=len(FibArray):
        print(FibArray)
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib