import math

n = int(input())

a = list(map(int,input().split()))
count = 0
for i in range(n):
    num = a[i]
    
    if num == 2 :
        count += 1
        continue
    
    is_prime = True
    for j in range(2, int(math.sqrt(num))+1):
        
        if num % j == 0:
            is_prime = False
            break

    if is_prime and num > 1:
        count += 1

print (count)