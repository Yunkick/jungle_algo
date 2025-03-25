import sys

def mult(a,b,c):
    if b == 1:
        return a % c
    
    elif b % 2 == 0:
        return (mult(a,b//2,c)**2)%c
    else:
        return ((mult(a,b//2,c)**2)*a)%c

x, y, z = map(int,sys.stdin.readline().split())

print(mult(x,y,z))