# https://www.acmicpc.net/problem/19532
# 백준 브론즈 2 19532번 수학은 비대면강의입니다

a,b,c,d,e,f = map(int,input().split())

for x in range(-999,1000):
    for y in range(-999,1000):
        if (a*x) + (b*y) == c and (d*x) + (e*y) == f:
            print(x,y)
            break
