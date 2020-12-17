def areFollowingPatterns(strings, patterns):
    s=strings.copy()
    p= patterns.copy()
    ds={k:v for k,v in zip(strings,patterns)}
    dp={k:v for k,v in zip(patterns,strings)}
    for i in range(len(patterns)):
        p[i]= dp[patterns[i]]
        s[i]= ds[strings[i]]      
    return (patterns == s) and (strings==p)
    
    

strings = ["cat", "dog", "cat", "dog"]
patterns = ["a","b", "a", "b"]

print(areFollowingPatterns(strings,patterns))


### solution from codeSignal
def followingPatterns(strings, patterns):
    return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))

