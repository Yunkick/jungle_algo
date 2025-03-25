import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    a = int(sys.stdin.readline())
    stack.append(a)

count = 0
max_ = 0

for i in stack[::-1]:
    if max_ < i:
        count += 1
        max_ = i

print(count)

 