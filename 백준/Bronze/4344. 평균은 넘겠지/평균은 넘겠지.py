c = int(input())

stu = []


for i in range (c):
    v= 0
    tt=0
    stu = list(map(int,input().split()))
    score = sum(stu[1::])
    average = score // (len(stu)-1)
    for j in stu[1:]:
        if j > average:
            v += 1
        tt = (v / (len(stu)-1)) 
    print('{:.3%}'.format(tt))