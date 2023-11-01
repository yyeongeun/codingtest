# 백준 1937번 욕심쟁이 판다
# DP 풀이
# https://www.acmicpc.net/problem/1937

import sys
sys.setrecursionlimit(999999999)
input = sys.stdin.readline

def recur(y,x):
    if dp[y][x] != 0: # dp 재사용하지 않기
        return dp[y][x]
    
    for dy, dx in [[0,-1],[0,1],[-1,0],[1,0]]: # 상하좌우 이동
        # 현재위치 y,x => ey,ex로 좌표이동
        ey = y + dy
        ex = x + dx        
        
        if 0 <= ey < n and 0 <= ex < n : # 그래프 넘어가면 무시
            if graph[y][x] < graph[ey][ex]: # 이동 가능한 경우
                dp[y][x] = max(dp[y][x], recur(ey,ex) + 1)
    return dp[y][x]

n = int(input()) # 대나무 숲의 크기
graph = [list(map(int,input().split())) for _ in range(n)] # 대나무 숲의 정보    
dp = [[0 for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        recur(y,x)

print(max(map(max,dp)) + 1) # 2차원 최대값 + 1
