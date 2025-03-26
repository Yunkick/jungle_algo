import sys

input_str = sys.stdin.readline().strip()
stack = []
result = 0
temp = 1

for i in range(len(input_str)):
    char = input_str[i]

    if char == "(":
        stack.append(char)
        temp *= 2

    elif char == "[":
        stack.append(char)
        temp *= 3

    elif char == ")":
        if not stack or stack[-1] != "(":
            result = 0
            break
        if input_str[i - 1] == "(":
            result += temp
        stack.pop()
        temp //= 2

    elif char == "]":
        if not stack or stack[-1] != "[":
            result = 0
            break
        if input_str[i-1] == "[":
            result += temp
        stack.pop()
        temp //= 3

if stack:
    result = 0
print(result)

