# 백준 1520번 내리막 길
# DP 풀이
# https://www.acmicpc.net/problem/1520

def recur(y,x):
    if y == m-1 and x == n-1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    route = 0
    for dy, dx in [[0,1],[0,-1],[1,0],[-1,0]]:
        ey = y + dy
        ex = x + dx
        if 0 <= ey < m and 0 <= ex < n:
            if graph[y][x] > graph[ey][ex]: # 작은값으로 이동
                route += recur(ey,ex)
    dp[y][x] = route
    
    return dp[y][x]

m, n = map(int,input().split()) # 세로 m 가로 n
graph = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]

answer = recur(0,0) # 0,0 에서 시작
print(answer)
