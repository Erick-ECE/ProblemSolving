''' 
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
'''

# fuerza bruta (time limit exceeded)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(1,len(nums),1):
            if i!=j and nums[i]+nums[j]==target:
                return [i,j]

#fuerza bruta mejorada
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums),1):
            if nums[i]+nums[j]==target:
                return [i,j]


#input
nums = [2,7,11,15]
target = 9 #output: [0,1]
nums2= [3,3]
target= 6 #output [0,1]

#call
print(twoSum(nums,target))

##O(n)? #no funciona:
# def twoSuma(self, nums: List[int], target: int):
#     rev=sorted(nums, reverse= True)
#     r=[]
#     for i in rev:
#         if i<= target:
#             target= target-i
#             r.append(nums.index(i))
#     return r


#using a dictionary 
def twoSum(self, nums: List[int], target: int) -> List[int]:
    d= {nums[x]:x for x in range(len(nums))}
    for i in range(len(nums)):
        complement= target - nums[i]
        if complement in d and d[complement] != i:
            return [i,d[complement]]

print(twoSum(nums,target))



###################################




