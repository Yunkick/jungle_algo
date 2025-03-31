import sys
sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[0] * (N+1) for _ in range(N+1)]
visit = [0] * (N+1)
count = []
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def DFS(v):
    global count 
   
    visit[v] = 1
    # print(v, end=' ')
    count.append(v)
    
    for i in range(1, N+1):
        
        if graph[v][i] and visit[i] == 0:
            DFS(i)


DFS(1)
print(len(count)-1)
