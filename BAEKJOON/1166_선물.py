# 백준 1166번 선물
# https://www.acmicpc.net/problem/1166

N, L, W, H = map(int,input().split())
left, right = 0, max(L,W,H)

while left <= right:
    mid = (left+right)/2
    if (L//mid)*(W//mid)*(H//mid) <= N :
        left = mid
    else:
        right = mid
print("%.10f"%(right))
