# 1966번
# https://www.acmicpc.net/problem/1966

import sys
from collections import deque

test = int(input())
for i in range(test):
    n, m = map(int,input().split())
    q = deque(list(map(int,sys.stdin.readline().split())))
    count = 0
    
    while q :
        best = max(q) #현재의 최댓값
        front = q.popleft()
        m -= 1
        
        if best == front :
            count += 1
            if m < 0:
                print(count)
                break
        else:
            q.append(front)
            if m < 0 :
                m = len(q)-1
           
