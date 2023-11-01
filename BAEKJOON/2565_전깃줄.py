# 백준 2565번 전깃줄
# LIS 풀이
# https://www.acmicpc.net/problem/2565

n = int(input()) # 전깃줄의 개수
arr = [list(map(int,input().split())) for _ in range(n)] # 연결된 전깃줄 위치의 번호
arr.sort() # a를 기준으로 정렬
dp = [1 for _ in range(n)]

# i보다 더 이전의 값에서 끝나는 전봇대 = 겹침
for i in range(1,n):
    for j in range(0,i):
        if arr[i][1] > arr[j][1]: # 안 겹친다면
            dp[i] = max(dp[i], dp[j]+1)

# 8-5 = 3
print(n-max(dp)) # 전체개수 - 안겹치는 최대 개수 = 없애야하는 전봇대 최소 개수
