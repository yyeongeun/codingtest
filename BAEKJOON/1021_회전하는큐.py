# 1021번
# https://www.acmicpc.net/problem/1021

import sys
from collections import deque

input = sys.stdin.readlilne()
n, m = map(int,input().split())#큐의 크기 n , 뽑아내려고하는 수 m
loc = list(map(int,input().split()))
q = deque([ _ for _ in range(1,n+1)])

count = 0
for i in loc:
    while True:
        if q[0] == i: #가장 최소위치가 가장 앞이라면 앞에 있는 원소 다 삭제
            q.popleft()
            break
        else:
            if q.index(i) < len(q)/2: #q의 i번째 위치 < q 길이의 절반
                while q[0] != i: #q의 첫번째 원소가 i가 될때까지 반복
                    q.append(q.popleft()) # 맨왼쪽 원소를 맨 뒤로 보내기
                    count += 1
            else:
                while q[0] != i :
                    q.appendleft(q.pop()) # 맨오른쪽 원소를 맨 앞으로 보내기
                    count += 1
print(count)
