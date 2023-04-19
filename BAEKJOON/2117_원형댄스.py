# 백준 2117번 원형 댄스
# https://www.acmicpc.net/problem/2117

n = int(input())

if n <= 2:
    print(0)
elif n == 3:
    print(1)
else:
    start = 2
    d = 2
    cnt = 0
    for i in range(n-4):
        start += d
        cnt += 1
        if cnt == 2:
            cnt = 0
            d += 1
    print(start)
