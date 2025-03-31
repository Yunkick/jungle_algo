import sys

N , M, V = map(int,sys.stdin.readline().split())

graph = [[0] * (N+1) for _ in range(N+1)]
visit1 = [0] * (N+1)
visit2 = visit1.copy()
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    visit1[v] = 1
    print(v , end=' ')
    for i in range(1, N+1):
        if graph[v][i] and visit1[i] == 0:
            dfs(i)

def bfs(v):
    queue = [v]
    visit2[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            if graph[v][i] and visit2[i] == 0:
                queue.append(i)
                visit2[i] = 1



dfs(V)
print()
bfs(V)
