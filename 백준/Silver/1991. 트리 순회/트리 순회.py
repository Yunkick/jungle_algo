n = int(input())
tree = {}

for i in range(n):
    root, left , right = map(str,input().split())
    tree[root] = left, right


def pre_order(v):
    if v != ".":
        print(v, end="")
        pre_order(tree[v][0])
        pre_order(tree[v][1])

def mid(v):
    if v != ".":
        mid(tree[v][0])
        print(v, end="")
        mid(tree[v][1])

def 후위(v):
    if v != ".":
        후위(tree[v][0])
        후위(tree[v][1])
        print(v, end="")


pre_order('A')
print("")
mid('A')
print("")
후위('A')
print("")