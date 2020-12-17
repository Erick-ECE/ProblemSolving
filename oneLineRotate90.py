#rotate 90°

def rotate(a):
    return [j[::-1] for j in [list(i) for i in zip(*a)]]

  
# Function to print the matrix 
def printMatrix(A): 
    N = len(A[0]) 
    for i in range(N): 
        print(A[i]) 
  
# Driver code 
A = [[1, 2, 3, 4], 
     [5, 6, 7, 8],  
     [9, 10, 11, 12],  
     [13, 14, 15, 16]] 

printMatrix(rotate(A))