# 백준 1149번 RGB거리
# https://www.acmicpc.net/problem/1149

n = int(input()) # 집의 수
price = [list(map(int,input().split())) for _ in range(n)] # 빨,초,파 비용

for idx in range(1,n):
    for rgb in range(3):
        if rgb == 0: # 빨
            price[idx][0] = min(price[idx-1][1],price[idx-1][2]) + price[idx][0]
        if rgb == 1: # 초
            price[idx][1] = min(price[idx-1][0],price[idx-1][2]) + price[idx][1]
        if rgb == 2: # 파
            price[idx][2] = min(price[idx-1][0],price[idx-1][1]) + price[idx][2]

print(min(price[n-1]))
