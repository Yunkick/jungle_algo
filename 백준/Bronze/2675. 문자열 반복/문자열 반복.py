n = int(input())

for i in range (n):
    arr = []
    a, b = (input().split())
    a = int(a)
    for j in range(len(b)):    
        arr.append(b[j] * a)
    print("".join(arr))