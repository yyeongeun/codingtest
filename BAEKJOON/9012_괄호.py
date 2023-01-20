# 9012번
# https://www.acmicpc.net/problem/9012
n = int(input())

for i in range(n):
    stack = []
    ans = True
    vps = input()
    for j in range(len(vps)):
        if vps[j] == '(':
            stack.append(vps[j])
        elif vps[j] == ')' and len(stack)>=1:
            stack.pop()
        else:
            ans = False
            break

    if len(stack) == 0 and ans == True:
        print("YES")
    else:
        print("NO")
