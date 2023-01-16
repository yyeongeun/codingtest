#4949번
#https://www.acmicpc.net/problem/4949
while True:
    a = input()
    stack = []
    if a == '.':
        break
    
    for i in a:
        if i == '(' or i =='[':
            stack.append(i)
        elif i ==')':
            if len(stack)!=0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack)!=0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) != 0:
        print("no")
    else:
        print("yes")
