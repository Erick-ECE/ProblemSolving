#House Robber
def rob(nums):
    # base cases:
    lnums = len(nums)
    if lnums == 0:
        return 0
    elif lnums == 1:
        return nums[0]
    elif lnums == 2:
        return max(nums[0],nums[1])
    elif lnums == 3:
        return max(sum(nums[::2]),nums[1])
    elif lnums == 4:
        return max(sum(nums[::2]),sum(nums[1::2]),nums[0]+nums[-1])
        
    candidates=[]
    candidates.append(nums[0])
    candidates.append(max(nums[1],candidates[0]))
    for i in range(2,len(nums)):
        print(candidates)
        candidates.append(max(nums[i]+candidates[i-2],candidates[i-1]))
    return candidates[-1]

houses1 = [10,20,2,3,50,15] # -> 70
houses2 = [1,2,3,1] # -> 4
houses3 = [2,7,9,3,1] #-> 12
houses4 = [2,1,1,2] # -> 4
houses5 = [4,1,2,7,5,3,1] # -> 14


rob(houses1)
rob(houses2)
rob(houses3)
rob(houses4)
rob(houses5)
