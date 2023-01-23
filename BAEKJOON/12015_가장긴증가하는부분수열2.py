# 12015번
# https://www.acmicpc.net/problem/12015

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = [0]

for i in a:
    if ans[-1] < i:
        ans.append(i)
    else:
        start = 0
        end = len(ans)
        
        while start < end:
            mid = (start+end)//2
            if ans[mid] < i:
                start = mid+1
            else:
                end = mid
        ans[end] = i
print(len(ans)-1)
