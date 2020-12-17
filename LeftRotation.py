# rota los elementos a la izquierda d veces
'''
input format:
n d # for n the length of the arrey and d the number of rotations
[e1, e2 ,...] # a list of inters
'''

# solution with linear memory
n,d = map(int, input().strip().split()) 
arr = list(map(int, input().strip().split()))

def leftRot(arr):
    ls = [0]*n
    for i in range(len(arr)):
        ls[i-d%n] = arr[i]
    return ls

'''Explanation:
    create 'ls' to save the new order of the elements
    
    'i-d%n' is the new position for each element of arr from the begining
    because 'i' is the position of de element '-d' the number of places that 
    should be moved to the left ('-' because is to the left)

    '%n' to be in range of the list 'arr' other way could happen an out of range Error
'''

# constant memory

def lRot(arr):
    return arr[d%n:] + arr[:d%n]

'''Explanation
    first sublist from the first rotated element to last in list 'arr'
    concatenade whith the missing elements from the start to the first rotated element
'''