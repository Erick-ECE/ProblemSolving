# kadane's algorithm
# max sum subarray
def kadenes(arr):
    msf=float('-inf') #max so far
    meh=0 # max end here
    for i in arr:
        meh=meh+i
        if i>meh:
            meh=i
        if meh>msf:
            msf=meh
    return msf

a= [-2, 2, 5, -11, 6] # awnser = 7
b= [-3, -2, -1, -4] # awnser= -1
print(kadenes(b))

# brute force


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

suma=float('-inf')
for i in range(len(arr)):
    temp=[]
    temp.append(arr[i])
    #print(temp)
    suma = max(suma,sum(temp))
    for j in arr[i+1:]:
            temp.append(j)
            #print(temp)
            suma = max(suma,sum(temp))

print(suma)
