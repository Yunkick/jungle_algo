import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())

graph  = []

for _ in range(N):
    a = list(map(int,sys.stdin.readline().strip()))
    graph.append(a)

def BFS(x,y): # BFS는 무조건 큐를 사용 한다는걸 알아야함
    queue = deque()
    queue.append((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or ny >= M or nx >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))


    return graph[N-1][M-1]

print(BFS(0,0))
