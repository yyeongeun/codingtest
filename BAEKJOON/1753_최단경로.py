# 백준 1753번 최단경로
# 다익스트라 BFS 알고리즘
# https://www.acmicpc.net/problem/1753

import heapq

N,M = map(int,input().split()) # 정점개수, 간선개수
start = int(input()) # 시작 번호

links = [[] for _ in range(N+1)] # input
dist = [1e9 for _ in range(N+1)] # 가까운 거리먼저 탐색해야함

for _ in range(M):
    A,B,C = map(int,input().split())
    links[A].append([B,C])

# BFS
# start 먼저 방문
q = []
heapq.heappush(q,[0,start]) # [현재의 가중치 0, 시작노드 start]
dist[start] = 0 # 시작점은 0 출력하라고 했음

while q:
    # 시작점으로부터 거리가 짧은 순서대로 방문 = heappop
    _w,node = heapq.heappop(q)
    
    for nxt, weight in links[node]:
        # 가중치는 작은 것으로 방문한다.
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q,[dist[nxt],nxt]) # 가중치 업데이트
         
for j in range(1,N+1):
    if dist[j] == 1e9:
        print("INF")
    else:
        print(dist[j])
