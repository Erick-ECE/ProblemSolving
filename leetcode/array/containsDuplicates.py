#contains duplicates
#given an array retur T | F if the rray contains duplicates

def containsDuplicates(arr):
    ndup=set(arr)
    return list(ndup) != arr