# array manipulation
'''
Starting with a 1-indexed array of zeros and a list of operations, 
for each operation add a value to each of the array element between two given indices,
 inclusive. Once all operations have been performed, return the maximum value in the array.
'''

n,nq= map(int, input().strip().split())
querrys=[]#consultas [inicio,final,valor]
for i in range(nq):
    querrys.append(list(map(int, input().split())))

arr=[0]*(n+1)

for q in querrys:
    arr[q[0]-1] += q[2] # q[0]-1 because they starts the index=1
    
    if q[1]<len(arr):
        try:
            arr[q[1]] -= q[2]
        except:
            pass

temp=0
for j in range(len(arr)):
    temp += arr[j]
    arr[j] = temp

print(max(arr))

    
    
