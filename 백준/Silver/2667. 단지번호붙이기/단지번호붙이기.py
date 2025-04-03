import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    a = list(map(int,sys.stdin.readline().strip()))
    graph.append(a)

visited = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def DFS(x,y):
    visited[x][y] = True
    count = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < N and 0<= ny < N:
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                count += DFS(nx,ny)
                
    return count

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            result.append(DFS(i,j))

result.sort()
print(len(result))
for n in result:
    print(n)