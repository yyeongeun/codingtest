# https://www.acmicpc.net/problem/1816
# 백준 브론즈 1 1816번 암호 키

N = int(input())
for _ in range(N):
    S = int(input())
    for i in range(2,1000001):
        if S%i == 0:
            print("NO")
            break
        if i == 1000000:
            print("YES")
