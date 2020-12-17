''' 
Return the sum of the numbers in the array,except ignore sections of
numbers starting with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). Return 0 for no numbers.
'''
# WORKS
def sum67(nums):
    if 6 in nums:
        t=nums.index(6)
        return sum67(nums[:t] + nums[nums.index(7,t)+1:])
    else:
        return sum(nums)

sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])
sum67([2, 7, 6, 2, 6, 2, 7])

# list.index(NtoFind,FROM,TO) // las tow parameters are the range to lookfor
