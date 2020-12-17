# is anagram? 

def isAnagram(s,u):
    return sorted(s) == sorted(u)

string1= "calabaza"
string2= "labzaaca"
string3= "calabazaaa"

print(isAnagram(string1,string2))
