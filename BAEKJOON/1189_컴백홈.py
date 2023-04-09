# 백준 1189번 컴백홈
# https://www.acmicpc.net/problem/1189

dx = [-1,0,1,0]
dy = [0,-1,0,1]

from collections import deque

def DFS(x,y,count):
    global answer
    visited[x][y] = 1
    if [x,y] == [0,c-1]: #오른쪽 맨 윗(집)도착시
        if count == k: #거리가 k라면 조건만족
            answer += 1
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<r and 0<=ny<c and visited[nx][ny] == 0 and graph[nx][ny] != "T":
            visited[nx][ny] = 1
            DFS(nx,ny,count+1)
            visited[nx][ny] = 0


r,c,k = map(int,input().split()) #행, 열, 거리
graph = [list(input()) for _ in range(r)] #집까지 가는 길 배열
visited = [[0 for _ in range(c)]for _ in range(r)] #방문여부
answer = 0
DFS(r-1,0,1) #왼쪽 맨 아래에서 시작
print(answer)         
