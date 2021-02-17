#LONGEST COMMON PREFIX

#Example:
#Input: strs = ["flower","flow","flight"]
#Output: "fl"

def lcp(words):
    #words.sort()
    model=words[0]
    lm= len(model)
    prefix=''
    #count=0
    for l in range(len(model)):
        for e in range(1,len(words)):
            if l<len(words[e]):
                if words[e][l] != model[l]:
                    return prefix
                elif words[e][l] == model[l]:
                    prefix += words[e][l]
            else:
                break
    return prefix

strs = ["flower","flow","flight","flojera"]
strs = ["dog","racecar","car"]
strs = []
lcp(strs)


def prueba(words):
    model=words[0]
    lm= len(model)
    prefix=''
    for l in range(len(model)):
        for e in range(1,len(words)):
            if l<len(words[e]):
                if words[e][l] != model[l]:
                    return prefix

        if l<len(words[e]):
            if words[e][l] == model[l]:
                prefix += words[e][l]
            #print("letra: %s  mprefix: %s  " % (words[e][l],model[l]))

prueba(strs)