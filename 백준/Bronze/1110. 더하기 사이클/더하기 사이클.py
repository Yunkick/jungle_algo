
n = int(input())

original = n  # 처음 입력값 저장
count = 0
x = n  # 변수를 따로 저장

while True:
    a = x % 10  # n 의 뒷자리를 뽑는 과정
    b = (x // 10 + x % 10) % 10  #새로운 수의 뒷자리를 뽑는 과정
    x = a * 10 + b  # 새로운수
    count += 1 
    
    if x == original: 
        break

print(count)
