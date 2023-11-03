# 백준 2606번 바이러스
# BFS 알고리즘 풀이
# https://www.acmicpc.net/problem/2606

from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
while q:
    node = q.popleft()
    visited[node] = 1
    for nxt in graph[node]:
        if visited[nxt] == 0:
            q.append(nxt)
        
print(sum(visited)-1)
