import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

left = 0
right = n - 1
total = 0
min_value = float('inf')
best = []

while left<right:
   
    left_ = arr[left]
    right_ = arr[right]
    total = left_ + right_

    if abs(total) < min_value:
        min_value = abs(total)
        best = [left_ , right_]


    if total < 0:
        left += 1
    else:
        right -= 1 

print(best[0], best[1])
