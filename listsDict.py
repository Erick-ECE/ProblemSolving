
words = input().split()

d = {x:words.count(x) for x in words}

w= dict()
w = {x:w.get(x,0)+1 for x in words}


n = int(input())

querys = []
for i in range(n):
    querys = list(input().strip().split[0])


L = []
for _ in range(int(input())):
    command, *args = input().split()
    try:
        getattr(L, command)(*(int(x) for x in args))
    except AttributeError:
        print(L)