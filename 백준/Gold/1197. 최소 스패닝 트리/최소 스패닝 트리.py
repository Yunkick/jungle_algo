import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)

V , E = map(int, input().split())

edges = []
for _ in range(E):
    A, B, C = map(int,sys.stdin.readline().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a,b):
    return get_parent(a) == get_parent(b)

total = 0
for a, b, cost in edges:
    if not same_parent(a,b):
        union_parent(a,b)
        total += cost
print(total)