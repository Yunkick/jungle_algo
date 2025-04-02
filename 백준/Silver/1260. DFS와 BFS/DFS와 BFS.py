import sys
from collections import deque
N, M, V = map(int,sys.stdin.readline().split())

graph= [[] for _ in range(N+1)]
visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

def DFS(v):
    visited1[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if not visited1[i]:
            DFS(i)

def BFS(v):
    visited2[v] = 1
    queue = deque([v])
    
    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for i in graph[node]:
            if visited2[i] == 0:
                visited2[i] = 1
                queue.append(i)



DFS(V)
print()
BFS(V)