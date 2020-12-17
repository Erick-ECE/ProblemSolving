# matrixElementsSum
'''
sum the elements in the matix, except the once that are under a 0
[[1,2,3]
 [0,5,0]   --->   sum(1,2,3,5,8) = 19
 [7,8,9]]
'''

def matrixElementsSum(matrix):
    from itertools import takewhile
    tranpose= list(zip(*matrix)) # traspose matrix takes the colimns as rows
    return sum([sum(takewhile(lambda x: x>0 , y)) for y in tranpose])


#tests cases:

m1 = [[1,2,3],[0,5,0],[7,8,9]]

print(matrixElementsSum(m1))