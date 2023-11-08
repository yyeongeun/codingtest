# 백준 1197번 최소 스패닝 트리
# 프림(다익스트라) 풀이
# https://www.acmicpc.net/problem/1197
import heapq
v,e = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(v+1)]
visited = [0 for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split()) # 정점 a,b 가중치 c
    graph[a].append([c,b])
    graph[b].append([c,a])

# 다익스트라 탐색
answer = 0
cnt = 0
q = [[0,1]] # 1에서 출발할거다. 가중치 없이
while q: # q가 아무것도 없어질 때까지
    if cnt == v:
        break
        
    weight, node = heapq.heappop(q) # 최소비용 꺼내주기
    if visited[node] == 0:
        visited[node] = 1        
        answer += weight
        cnt += 1
        for nxt in graph[node]:
            heapq.heappush(q,nxt)
print(answer)
