a = int(input())
b = int(input())
c = int(input())


v = 0
d = a * b * c
d_str = str(d)

count = [0] * 10

for digit in d_str:
    count[int(digit)] +=1
for i in range(10):
    print(count[i])
  