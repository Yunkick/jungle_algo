import sys
from collections import deque

n , m, k, x= map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [-1] * (n+1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

def BFS(v):
    visited[v] = True
    q = deque([v])
    distance[v] = 0
    answer = []

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                distance[i] = distance[now] + 1

            if distance[i] == k and i not in answer:
                answer.append(i)

    if answer:
        answer.sort()
        for i in answer:
            print(i)
    else:
        print(-1)
       
        


BFS(x)