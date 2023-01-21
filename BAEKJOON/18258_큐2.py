# 18258번
# https://www.acmicpc.net/problem/18258

import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    c = sys.stdin.readline().split()
    
    if c[0] == 'push': # 큐에 넣기
        queue.append(c[1])
        
    elif c[0] == 'pop': # 큐에서 가장 앞에 있는 정수 빼내고 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
            
    elif c[0] == 'size': # 큐 정수개수 출력
        print(len(queue))
        
    elif c[0] == 'empty': # 큐 비어있는지 확인
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front': #큐 가장 앞에 있는 정수 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif c[0] == 'back': #큐 가장 뒤에 있는 정수 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
