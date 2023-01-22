# 11866번
# https://www.acmicpc.net/problem/11866

from collections import deque

n, k = map(int, input().split())

queue = deque()
for i in range(1, n+1):
    queue.append(i)

answer = []
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")
