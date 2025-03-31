import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M = map(int,sys.stdin.readline().split())

graph = []


for _ in range(N):
    b = list(map(int, list(sys.stdin.readline().strip())))
    graph.append(b)


def BFS(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

            if nx == N-1 and ny == M-1:
                return graph[nx][ny]

print(BFS(0,0))   
