n = 7
p = [0]*(n+1)


def makeSet():
    for i in range(n+1):
        p[i] = i


def findSet(x):
    if x == p[x]:
        return x
    else:
        p[x] = findSet(p[x])
        return p[x]


def union(x, y):
    p[findSet(y)] = findSet(x)


makeSet()
for i in range(7):
    case, x1, y1 = map(int, input().split())
    if case == 0:
        union(x1, y1)
    else:
        if findSet(x1) == findSet(y1):
            print("YES")
        else:
            print("NO")
