# read the file input.txt
data = open('/home/usuario/Documentos/HackerRank/input.txt','r')

nodes,edges = data.readline().strip().split()

aristas = []
for row in data:
    aristas.append(list(map(int, row.strip().split())))

print(aristas)