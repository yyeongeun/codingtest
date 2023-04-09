# 백준 1012번 유기농 배추
# https://www.acmicpc.net/problem/1012

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):           
    queue = [(x,y)]
    graph[x][y] = 0 # 방문처리

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1 : #방문하지 않았다면
                queue.append((nx,ny))
                graph[nx][ny] = 0

T = int(input()) #테스트케이스의 개수
for i in range(T):
    M, N, K = map(int,input().split()) #배추밭 가로길이, 세로길이, 배추위치
    graph = [[0]*(N) for _ in range(M)]
    cnt = 0

    for j in range(K):
        x,y = map(int, input().split()) #배추좌표
        graph[x][y] = 1 #배추 있다는 표시

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                BFS(a,b)
                cnt += 1

    print(cnt)
