import sys

a = int(sys.stdin.readline())

arr = []

for i in range(a):
    arr.append(sys.stdin.readline().strip())


arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)
