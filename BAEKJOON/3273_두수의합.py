# 백준 3273번 두 수의 합
# 투포인터 알고리즘
# https://www.acmicpc.net/problem/3273

n = int(input())
arr = sorted(list(map(int,input().split())))
x = int(input())

# 투포인터
s = 0
e = n-1

cnt = 0

while s < e:
    if arr[s] + arr[e] == x:
        cnt += 1
    if arr[s] + arr[e] >= x:
        e -= 1
    else:
        s += 1
print(cnt)
