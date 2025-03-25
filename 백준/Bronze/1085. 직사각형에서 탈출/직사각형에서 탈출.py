x, y, w, h = map(int,input().split()) 

a = abs(x - w)
b = abs(y - h)
c = abs(x - 0)
d = abs(y - 0)


b = a if a < b else b
c = b if b < c else c
d = c if c < d else d



   



print (d)

