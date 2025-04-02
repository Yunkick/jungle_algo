import sys
from collections import deque
K = int(sys.stdin.readline())

def gr():
    V , E = map(int,sys.stdin.readline().split())
    color = [0] * (V+1)
    g = [[] for _ in range(V+1)]
    
    for _ in range(E):
        a, b = map(int,sys.stdin.readline().split())
        g[a].append(b)
        g[b].append(a)

    for i in range(1, V+1):
        if color[i] == 0:
            q = deque([i])
            color[i] = 1

            while q:
                now = q.popleft()
                for next in g[now]:
                    if color[next] == 0:
                        color[next] = 3 - color[now]
                        q.append(next)
                    elif color[next] == color[now]:
                        return "NO"
                
    return 'YES'

for _ in range(K):
    print(gr())


