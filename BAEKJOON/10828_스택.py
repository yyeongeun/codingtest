#10828번
#https://www.acmicpc.net/problem/10828

#import sys
n = int(input())
command = [list(map(str,input().split())) for _ in range(n)]

stack = []

for i in range(n):
    #command = sys.stdin.readline().split()
    
    if command[i][0] == 'push':
        stack.append(command[i][1])
    elif command[i][0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[i][0] == 'size':
        print(len(stack))
    elif command[i][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[i][0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])       
    
