# 백준 11053번 가장 긴 증가하는 부분 수열
# LIS 문제
# https://www.acmicpc.net/problem/11053

n = int(input())
arr = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i): # 내 기준 왼쪽에 있는 숫자까지 확인
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
