n = int(input())

a = list(map(int,input().split()))

m = int(input())

b = list(map(int,input().split()))
a.sort()
num = 0

# b = [10, 9, -5, 2, 3, 4, 5, -10]
num = 0
def search (arr, target):
    left = 0
    right = len(arr)-1
    

    while left <= right:
        mid = (left + right)//2

        if arr[mid] == target:
            return 1
        
        if arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1

    
    return 0

for i in range(len(b)):
    
    print(search(a,b[i]))