# solutuion from geeksForGeeks
def rotate90Clockwise(A): 
    N = len(A[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            #print(i,j)
            temp = A[i][j] 
            A[i][j] = A[N - 1 - j][i] 
            #print(A[N - 1 - j][i])
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j] 
            #print(A[N - 1 - j][i])
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
            A[j][N - 1 - i] = temp 
  
# Function to print the matrix 
def printMatrix(A): 
    N = len(A[0]) 
    for i in range(N): 
        print(A[i]) 
  
# Driver code 
a = [[1, 2, 3, 4], 
     [5, 6, 7, 8],  
     [9, 10, 11, 12],  
     [13, 14, 15, 16]] 
rotate90Clockwise(a) 
printMatrix(a) 
##################################################################
# my solution space:O(n)
def rotateImage(a):
    dup= []
    for i in range(len(a)):
        for j in range(len(a)-1,-1,-1):
            dup.append(a[j][i])
            
    for i in range(len(a)-1,-1,-1):
        for j in range(len(a)-1,-1,-1):
            a[i][j] =  dup.pop()
    return a

b = rotateImage(A)

printMatrix(b)

