# 3Sum
# given an array of n inregers are there elements a,b,c in nums
# such that a+b+c=0
# find all the triplets in the array which gives 0

nums= [-1,0,1,2,-1,-4]
nums2= []
nums3=[0]

def threeSum(arr):
    arr.sort()
    result=[]
    for i in range(len(arr)-1):
        a = arr[i]
        start=i+1
        end=len(arr)-1
        while start<end:
            b = arr[start]
            c = arr[end]
            if a+b+c==0:
                if [a,b,c] not in result:
                    result.append([a,b,c])
                start += 1
                end -= 1
            elif a+b+c>0:
                end-=1
            else:
                start+=1
    return result

threeSum(nums)