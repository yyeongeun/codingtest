# 백준 12865번 평범한 배낭
# 탑다운 DP 방식
# https://www.acmicpc.net/problem/12865

def recur(idx,w):    
    if w > k: # 버틸 수 있는 k 무게 초과시 무시
        return -9999999999
    if idx == n: # 모든 물품 사용
        return 0
    if dp[idx][w] != -1:
        return dp[idx][w]

    # 해당 물품 넣은/안넣은 경우
    dp[idx][w] = max(recur(idx+1, w+list_a[idx][0]) + list_a[idx][1],recur(idx+1, w))
    
    return dp[idx][w]

n, k = map(int,input().split()) # 물품의 수, 버틸 수 있는 무게
# 각 물건의 무게 w, 해당 물건의 가치 v
list_a = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1 for _ in range(100001)] for _ in range(n)]
recur(0,0) #물품 번호 0, 물건의 무게 0
print(dp[0][0])
