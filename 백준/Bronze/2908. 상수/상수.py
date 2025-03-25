a, b= map(int,input().split())
c = str(a)[::-1]
d = str(b)[::-1]


if int(c) < int(d) :
    print (d)
else:
    print (c)