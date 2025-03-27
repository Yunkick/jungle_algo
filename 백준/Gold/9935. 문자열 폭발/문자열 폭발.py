a = input().strip()
bomb = input().strip()
bomb_len = len(bomb)

stack = []
for i in range(len(a)):
    stack.append(a[i])
    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

if stack:

    print("".join(stack))
else:
    print("FRULA")