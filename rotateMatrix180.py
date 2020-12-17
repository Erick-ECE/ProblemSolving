# rotate matrix 180°

def rotate180(a):
    size=len(a)
    for i in range(size-1,size//2,-1): # Swipe the rows (horizontal mirror)
        temp= a[(size-1)-i]
        a[(size-1)-i] = a[i]
        a[i]= temp
    for i in range(size):
        a[i]= a[i][::-1]

        

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

rotate180(A)
printMatrix(A)