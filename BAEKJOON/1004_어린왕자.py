# 백준 1004번
# https://www.acmicpc.net/status?user_id=zena0101&problem_id=1004&from_mine=1

T=int(input())
for _ in range(T):
    x1, y1, x2, y2 = list(map(int,input().split())) #출발점, 도착점
    n = int(input()) # 행성계 개수
    cnt = 0
    for _ in range(n):
        cx, cy, cr = map(int,input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2
        d2 = (x2-cx)**2 + (y2-cy)**2
        pow_cr = cr**2
        if pow_cr > d1 and pow_cr > d2:
            pass
        elif pow_cr > d1:
            cnt += 1
        elif pow_cr > d2:
            cnt += 1
    print(cnt)
