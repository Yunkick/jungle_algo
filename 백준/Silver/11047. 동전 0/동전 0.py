import sys
n , k = map(int,sys.stdin.readline().split())

money = []

for _ in range(n):
    a = int(sys.stdin.readline())
    money.append(a)

money.sort(reverse=True)

result = 0

for i in money:
    if k == 0:
        break
    result += k//i
    k %= i

print(result)