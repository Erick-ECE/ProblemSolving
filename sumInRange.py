# Sum in range
'''
You have an array of integers nums and an array queries, where queries[i] 
is a pair of indices (0-based). Find the sum of the elements in nums from
the indices at queries[i][0] to queries[i][1] (inclusive) for each query, 
then add all of the sums for all the queries together. 
Return that number modulo 109 + 7.
'''
'''
For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], the output should be
sumInRange(nums, queries) = 10.
'''

# timelimit exceeded
def sumInRange(nums, queries):
    sumas=0
    for i in queries:
        sumas+= sum(nums[i[0]:i[1]+1]) 
    return sumas%((10**9)+7)


#sol2:
#make an acumulative sum (the sum of a range is nums[j]-nums[i-1] for i<j) for a acumulative sumed array

def sumInrange(nums,queries):
    for i in range(len(nums)-1): # make the acumulative sum
        nums[i+1]+=nums[i]
    print(nums)
    suma=0
    for i in queries: #since queries[0] has de start of the subarray
        if queries[0]==0:
            suma+=nums[i[1]] # nums at position i-query[1] has already the sum of nums[0:i[1]]
        else:
            suma += nums[i[1]] - nums[i[0]-1] 
    return suma




nums = [-2, 2, 5, -11, 6] 
queries = [[1, 2]]

print(sumInrange(nums,queries))

