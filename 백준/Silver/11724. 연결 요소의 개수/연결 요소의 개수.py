import sys
sys.setrecursionlimit(10**7)
N , M = map(int,sys.stdin.readline().split())

graph = [[0] * (N+1) for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1



def DFS(v):
    
    visit[v] = 1
    for i in range(1, N+1):
        if graph[v][i] and visit[i] == 0:
            DFS(i)

count = 0
for i in range(1, N+1):
    if not visit[i]:
        DFS(i)
        count += 1

print(count)