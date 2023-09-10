# https://www.acmicpc.net/problem/14568
# 백준 14568번 2017 연세대학교 프로그래밍 경시대회

N = int(input()) # 사탕 N개 
cnt = 0

for a in range(1,N-3): # 영훈
    for b in range(a+2, N-1): # 남규
        c = N-a-b # 택희
        if c >= 1 and c%2 == 0:
            cnt += 1
print(cnt)
