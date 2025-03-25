import sys
n = int(sys.stdin.readline())
paper = []

for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split()))) 

count = {0 : 0, 1: 0}
cut_count = 0
def check_color(x,y,size):
    first_color = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != first_color:
                return False
    return True


def count_color(x,y,size):
    if check_color(x,y,size):
        count[paper[x][y]] += 1
        
        return
    
    count_color(x,y,size//2)
    count_color(x+size//2 , y, size//2)
    count_color(x, y+size//2,size//2)
    count_color(x+size//2, y+size//2, size//2)
    
count_color(0,0,n)
print(count[0])
print(count[1])
