# 백준 14501번 퇴사
# 바텀업 DP, 점화식으로 문제 풀이
# https://www.acmicpc.net/problem/14501

n = int(input())
list_a = [list(map(int,input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for idx in range(n)[::-1]:
    if (idx+list_a[idx][0]) > n: # 범위 초과시
        dp[idx] = dp[idx+1]
    else:
        dp[idx] = max(dp[idx+list_a[idx][0]]+list_a[idx][1],dp[idx+1])
print(dp[0])
