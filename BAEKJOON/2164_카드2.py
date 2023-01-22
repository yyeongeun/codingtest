# 2164번
# https://www.acmicpc.net/problem/2164

import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([i for i in range(1,n+1)])

while (len(q)>1):
    q.popleft() #제일 위(왼쪽)에 있는 카드 버리기
    temp = q.popleft() #두번째 카드 저장하기
    q.append(temp)
    
print(q[0]) 
