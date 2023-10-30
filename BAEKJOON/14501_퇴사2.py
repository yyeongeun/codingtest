# 백준 14501번 퇴사
# 탑다운 DP 이용한 풀이
# https://www.acmicpc.net/problem/14501

import sys
sys.setrecursionlimit(99999999)
input = sys.stdin.readline

def recur(day):
    if day > n: # day = 0일부터 n-1일까지
        return -9999999999999
    if day == n:
        return 0
    
    # 이미 저장되었다면
    if dp[day] != -1:
        return dp[day]
    
    # 상담 받거나/안받거나 둘중 더 많은 돈을 버는 경우를 내 dp 테이블에 저장
    dp[day] = max(recur(day+list_a[day][0]) + list_a[day][1],recur(day+1))    
    return dp[day]

n = int(input()) # n일째
list_a = [list(map(int,input().split())) for _ in range(n)] # t,p
dp = [-1 for _ in range(n+1)]
recur(0) #0일부터 시작
print(dp[0])
