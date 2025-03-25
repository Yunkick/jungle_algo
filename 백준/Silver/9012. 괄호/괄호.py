T = int(input())

for _ in range(T):
    stack = []
    str = input()
    
    for c in str:
        if c == '(':
            stack.append(c)
        elif c == ')':
            
            if len(stack) != 0:
                stack.pop()
                
            else:
                print("NO")
                break
            
    
    else:        
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")     