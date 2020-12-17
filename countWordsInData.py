#histogram of data.txt

data = open("/home/usuario/Documentos/HackerRank/data.txt", 'r')

d = dict()
for line in data:
    words = line.split()
    for word in words:
        d[word] = d.get(word,0) + 1

print(d)

key,value = None,None
for k,v in d.items():
    if key is None or value < v:
        key = k
        value = v

print('key: {} value: {}'.format(key,value))