# 백준 2559번 수열
# https://www.acmicpc.net/problem/2559

n, k = map(int,input().split())
arr = list(map(int,input().split()))

prefix = [0 for _ in range(n+1)]
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]

answer = []
for i in range(k,n+1):
    answer.append(prefix[i] - prefix[i-k])

print(max(answer))
