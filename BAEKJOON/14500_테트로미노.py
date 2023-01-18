#14500번
#https://www.acmicpc.net/problem/14500

import sys
input = lambda : sys.stdin.readline()

def dfs(r, c, depth, total):
    global max_value
    if max_value >= total + board_max*(4-depth) :
        return        
    if depth >= 4:
        max_value = max(max_value,total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
                if depth == 2:
                    visited[nr][nc] = 1
                    dfs(r, c, depth + 1, total + board[nr][nc])
                    visited[nr][nc] = 0

                visited[nr][nc] = 1
                dfs(nr, nc, depth + 1, total + board[nr][nc])
                visited[nr][nc] = 0

# 입력
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 좌표 이동
dr = [-1,0,1,0]
dc = [0,1,0,-1]

board_max = max(map(max, board))
max_value = 0

# 하나씩 dfs 돌리기
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,board[i][j])
        visited[i][j] = 0

print(max_value)
