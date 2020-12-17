''' 

Return the sum of the numbers in the array, returning 0 for an empty array.
 Except the number 13 is very unlucky, so it does not count and
numbers that come immediately after a 13 also do not count.
'''
def sum13(nums):
    if nums == []: return 0
    total = 0
    for i in range(len(nums)):
        if nums[i] == 13 or nums[i-1] == 13:
            pass
        else:
            total+=nums[i]
        return total

## option 2

def sum13(nums):
  
print(sum13([1, 2, 13, 2, 1, 13]))