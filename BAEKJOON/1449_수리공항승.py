# 백준 1449번 수리공 항승
# https://www.acmicpc.net/problem/1449
import sys
input = sys.stdin.readline

N, L = map(int,input().split())
loc = list(map(int,input().split()))
loc.sort()
start = loc[0]
cnt = 1

for location in loc[1:]:
    if location in range(start,start+L):
        continue
    else:
        start = location
        cnt += 1
print(cnt)
