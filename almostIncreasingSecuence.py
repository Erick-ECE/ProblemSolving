#almost increasing secuence
'''
return True if by deleting at most one element in the secuence, the secuence still acending
return False if the secuence can't be acending deleting one element at most 
'''

def almostIncreasingSecuence(arr): # returns false if can't be an acending secuence
    last=prev = float('-inf')
    flag=False
    for elem in arr:
        print(prev,last,elem)
        print(flag)
        if elem<=last:
            if flag == True: # means there were an unsorted prv element
                return False
            flag=True
            if elem<=prev:
                prev=last
            elif elem>prev:
                prev=last=elem
        else:
            prev=last
            last=elem
    return True

#inputs
l = [1, 2, 5, 3, 5]

print("awnser: ",almostIncreasingSecuence(l))


'''
###first Solution

def almostIncreasingSequence(sequence):
    toDelete= float('-inf')
    for i in range(1,len(sequence)): # saca el posible elemento a borrar
        if sequence[i-1]>=sequence[i]:
            toDelete = i #segundo elemento 
            break
    print(toDelete)
    sec2 = sequence[:toDelete]+sequence[toDelete+1:] # borro el segundo elemento
    td2= float('-inf')
    for j in range(1,len(sec2)):
        if sec2[j-1]>=sec2[j]: # si el elemento 2 no era 
            td2 = j # primer elemento
    
    if td2 == float('-inf'):
        return True
    sec3 = sequence[:td2-1]+sequence[td2:] # borra el primer elemento 
    td3 = float('-inf')
    for k in range(1,len(sec3)):
        if sec3[k-1]>=sec3[k]:
            td3 = k
    if td3 == float('-inf'):
        return True
    return False        
            
        
        



'''

