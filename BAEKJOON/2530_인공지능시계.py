# https://www.acmicpc.net/problem/2530
# 백준 2530번 인공지능 시계

a,b,c = map(int,input().split()) # 현재 시,분,초
d = int(input()) # 더해야할 시간

bb = b + d//60
c += d%60
if bb > 60:
    a += bb//60
    b += bb%60
else:
    b = bb
print(a,b,c)
