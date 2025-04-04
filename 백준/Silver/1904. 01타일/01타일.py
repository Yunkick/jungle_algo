import sys
n = int(sys.stdin.readline())

g = [0] * 1000001
g[1] = 1
g[2] = 2


for i in range(3, n+1):
    g[i] = (g[i-1] + g[i-2])%15746
   
print(g[n])