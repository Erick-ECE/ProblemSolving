# kandene's algorithm
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