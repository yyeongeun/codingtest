# 백준 2606번 바이러스
# DFS 알고리즘 풀이
# https://www.acmicpc.net/problem/2606

n = int(input()) # 컴퓨터 수
m = int(input()) # 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]
# 각 노드에서 연결된 노드번호들 입력해준다.
# graph[1] = [2,5]
# graph[2] = [1,3,5]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b) # a -> b 연결
    graph[b].append(a) # b -> a 연결
    
def recur(node):
    visited[node] = 1
    for nxt in graph[node]: # 다음지점
        if visited[nxt] == 1: # 방문한 곳이라면 역주행 하지 않도록
            continue        
        recur(nxt) # 방문
        
recur(1)
print(sum(visited)-1)
