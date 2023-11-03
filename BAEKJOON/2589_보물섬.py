# 백준 2589번 보물섬
# BFS 알고리즘
# https://www.acmicpc.net/problem/2589

from collections import deque

n,m = map(int,input().split()) # 세로, 가로
graph = [list(input().rstrip()) for _ in range(n)] # 문자열

maxi = 0 # 보물 찾기에 가장 긴 시간

# 모든 graph 방문
for y in range(n):
    for x in range(m):
        if graph[y][x] == 'L': # 육지일때만 간다
            # 매번 방문여부/거리 초기화
            visited = [[0 for _ in range(m)] for _ in range(n)]
            dist = [[0 for _ in range(m)] for _ in range(n)]
            
            # BFS
            q = deque()
            q.append((y,x)) # 첫번째 값 방문
            visited[y][x] = 1 # 방문처리
            
            while q:
                ey, ex = q.popleft() # 현재 위치                
                # 4방향 상하좌우 탐색
                for dy, dx in [(1,0),(-1,0),(0,-1),(0,1)]:
                    # 이동 위치
                    ny = ey + dy
                    nx = ex + dx
                    # x와 y안에 있는지 & 육지인지 & 방문하지 않았는지
                    if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == "L" and visited[ny][nx] == 0:                         
                        visited[ny][nx] = 1 # 방문처리
                        # 현재까지의 거리 + 한 칸 추가, 새로운 값 중 큰 값으로 저장
                        dist[ny][nx] = max(dist[ey][ex]+1, dist[ny][nx])
                        if maxi < dist[ny][nx]: # maxi는 계속 최대값으로 업데이트
                            maxi = dist[ny][nx]
                        q.append((ny,nx)) # 새로운 위치로 방문
                                
print(maxi)
