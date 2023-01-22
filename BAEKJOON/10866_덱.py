# 10866번
# https://www.acmicpc.net/problem/10866
import sys
from collections import deque

d = deque()
n = int(input())

for i in range(n):
    c = sys.stdin.readline().split()
    
    if c[0] == 'push_front':
        d.appendleft(c[1]) #앞에 push = appendleft
    elif c[0] == 'push_back':
        d.append(c[1])
    elif c[0] == 'pop_front':
        if d:
            print(d[0])
            d.popleft()
        else:
            print("-1")   
    elif c[0] == 'pop_back':
        if d:
            print(d[len(d)-1])
            d.pop()
        else:
            print("-1")
    elif c[0] == 'size':
        print(int(len(d)))
    elif c[0] == 'empty':
        if d:
            print("0")
        else:
            print("1")
    elif c[0] == 'front':
        if d:
            print(d[0])
        else:
            print("-1")
    elif c[0] == 'back':
        if d:
            print(d[len(d)-1])
        else:
            print("-1")
