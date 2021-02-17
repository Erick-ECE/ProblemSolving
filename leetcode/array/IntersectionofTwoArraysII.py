# Given two arrays, write a function to compute their intersection.

def intersect(a,b):
    result=[]
    for i in a:
        if i in b:
            result.append(i)
            b.remove(i)
    return result

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1,nums2))