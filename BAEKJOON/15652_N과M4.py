# 15652번
# https://www.acmicpc.net/problem/15652

N, M = list(map(int,input().split()))
ans = []

def back(start):
    if len(ans) == M:
        print(" ".join(map(str,ans)))
        return
    for start in range(start,N+1):
        ans.append(start)
        back(start)
        ans.pop()
back(1)
