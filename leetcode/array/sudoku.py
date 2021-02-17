# valid sudoku check

#Aux function to check reps
def reps(l):
    return len([x for x in l if x!='.']) == len({x for x in l if x != '.'})
#Aux fun turbo
def repsT(l):
    s=set()
    l=[]
    for i in l:
        if i != '.':
            s.add(i)
            l.append(i)
    return len(l)==len(s)

#aux turbo+
def repP(l): #return true if No reps found
    d={}
    for i in l:
        if i != '.':
            d[i]=d.get(i,0)+1
    for i in d:
        if d[i]>1:
            return False
    return True
    
    

def sudoku(grid):
    #check for rows
    for row in grid:
        if not repP(row):
            return False
    print("no reps in row")
    #check in transpose(columns)
    for column in list(zip(*grid)):
        if not repP(column):
            return False
    print("no reps in column")
            
    #check in subgrid 3x3
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not repP(grid[i][i:i+3]+grid[i+1][i:i+3] + grid[i+2][i:i+3]):
                return False            
    return True
        

### Test:
#assert true
grid= [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

#assert false
grid2= [["8","3",".",".","7",".",".",".","."] 
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

#assert true
grid3= [[".",".",".","1","4",".",".","2","."], 
 [".",".","6",".",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".","1",".",".",".",".",".","."], 
 [".","6","7",".",".",".",".",".","9"], 
 [".",".",".",".",".",".","8","1","."], 
 [".","3",".",".",".",".",".",".","6"], 
 [".",".",".",".",".","7",".",".","."], 
 [".",".",".","5",".",".",".","7","."]]

print(sudoku(grid))