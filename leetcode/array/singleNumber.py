# Single Number
# given a non-empty array of integers,
# evrery element apears twice except one. Find that single one.
#input= [4,1,2,1,2]
#output= 4

def singleNumber(arr):
    single=arr[0]
    for i in range(1,len(arr)):
        single^=arr[i] # make a bitwise operation (xor) over all the array

    return single 