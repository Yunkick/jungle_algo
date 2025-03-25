import sys

n = int(sys.stdin.readline())

top = list(map(int,sys.stdin.readline().split()))

stack = []
result = []

for i in range(n):
    while stack and stack[-1][0] < top[i]:
        stack.pop()

    if stack:
        result.append(stack[-1][1])

    else:
        result.append(0)

    stack.append((top[i], i + 1))


print(" ".join(map(str, result)))