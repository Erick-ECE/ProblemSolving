#"Given an array of N numbers, for each index i,
# return the product of all numbers except the one at index i.
# For example [3,2,4,1] should return [8, 12, 6, 24]"

def foo(arr): #O(2n) O(n)
    tot= 1
    for i in arr: 
        tot*= i
    arr2=[]
    for i in arr:
        arr2.append(tot//i)
    return arr2

# O(n²) solution:

def foo2(arr):
    result=[]
    for i in range(len(arr)):
        temp=1
        for j in range(len(arr)):
            if i!=j:
                temp*=j
        result.append(temp)
    return result


