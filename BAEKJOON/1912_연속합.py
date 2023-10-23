# 백준 1912번 연속합
# https://www.acmicpc.net/problem/1912

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
prefix = [-1001]*(n+1)

for i in range(n):
    prefix[i+1] = max(prefix[i] + arr[i], arr[i])

print(max(prefix))
