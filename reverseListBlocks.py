# revers of the elements of a list
# Example
# ['O','n','e',' ','T','o','w',' ','T','h','r','e','e'] -> ['T','h','r','e','e',' ','T','o','w',' ','O','n','e']

def reveseList(arr):
    temp=''.join(arr).split()
    temp.reverse()
    return list(' '.join(temp))

example= ['O','n','e',' ','T','o','w',' ','T','h','r','e','e']

reveseList(example)