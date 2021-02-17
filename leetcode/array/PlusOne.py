# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Input: digits = [1,2,3]
# Output: [1,2,4]

# solucion de internet:
def plusOne1(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]<9:
            digits[i]=digits[i]+1
            return digits
        else:
            digits[i]=0
    result=[0]*(len(digits)+1)
    result[0]=1
    return result

print(plusOne1([9,9]))