# 백준 12865번 배낭
# 탑다운 DP, 점화식 풀이 방법
# https://www.acmicpc.net/problem/12865

n, k = map(int, input().split())

list_a = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    list_a.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for idx in range(1, n + 1):
    for weight in range(1, k + 1):        
        if weight < list_a[idx][0]:
            dp[idx][weight] = dp[idx - 1][weight]
        else:
            dp[idx][weight] = max(dp[idx - 1][weight - list_a[idx][0]] + list_a[idx][1],dp[idx - 1][weight])

print(dp[n][k])
