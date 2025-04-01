import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
visit = [False] * len(graph)
parent = [0] * len(graph)


for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



def DFS(v):
    visit[v] = True
    for next_node in graph[v]:
        if parent[next_node] == 0:
            parent[next_node] = v
            DFS(next_node)

DFS(1)
for i in range(2, N+1):
    print(parent[i])

