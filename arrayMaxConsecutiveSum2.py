'''
Given an array of integers, find the maximum possible sum you can get from 
one of its contiguous subarrays. The subarray from which this sum comes must 
contain at least 1 element.
'''
'''
Example:
inputArray = [-2, 2, 5, -11, 6], the output should be
arrayMaxConsecutiveSum2(inputArray) = 7
'''

# slow solution:+
def arrayMaxConsecutiveSum2(inputArray):
    for i in range(len(inputArray)-1):
        inputArray[i+1]+=inputArray[i]
    maxim=max(inputArray)
    
    for i in range(len(inputArray)):
        for j in range(i+1,len(inputArray),1):
            maxim= max(maxim,(inputArray[j]-inputArray[i]) )

    return maxim

# better solution
def arrayMaxConsecutiveSum2(inputArray):
    acSum=inputArray[0] 
    for i in range(len(inputArray)):
        inputArray[i+1]+=inputArray[i]
    maxim=max(inputArray)
