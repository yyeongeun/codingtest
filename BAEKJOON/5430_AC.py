# 5430번
# https://www.acmicpc.net/problem/5430

import sys
from collections import deque

t = int(input()) # 테스트 케이스 개수
for i in range(t):
    p = input().strip() #함수
    n = int(input()) #배열 수의 개수
    arr = input()[1:-1].strip().split(',') # 배열에 들어가있는 숫자들
    q = deque(arr)

    if n == 0: # 예외처리
        q = deque()
        
    R = 0 # R함수가 나온 횟수
    for j in p:
        if j == 'R':
            R += 1
        elif j == 'D': # 가장 왼쪽 값 삭제 popleft()
            if len(q) == 0:
                print('error')
                break
            else:
                if R % 2 == 0: #reverse 필요 없는 경우
                    q.popleft() 
                else: # reverse해야하는 경우라 가장 오른쪽 값 삭제
                    q.pop()

    else:
        if R % 2 == 0:
            print('[' + ",".join(q) + ']')
        else:
            q.reverse()
            print('[' + ",".join(q) + ']')
