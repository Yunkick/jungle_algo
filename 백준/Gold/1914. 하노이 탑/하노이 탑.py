n = int(input())

def hanoi(n, rod1, rod2, rod3):
    if n == 1:
        print(rod1, rod3)
    else:
        hanoi(n-1, rod1, rod3, rod2)
        print(rod1, rod3)
        hanoi(n-1, rod2, rod1, rod3)

if n <= 20:
    print(2**n - 1)  # 이동 횟수 출력
    hanoi(n, 1, 2, 3)  # 이동 경로 출력
else:
    print(2**n - 1)  # 이동 횟수만 출력
