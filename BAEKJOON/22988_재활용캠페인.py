# 백준 22988번 재활용 캠페인
# 투포인터 알고리즘
# https://www.acmicpc.net/problem/22988

n, x = map(int,input().split()) # 용기의 수, 용기의 총 용량
arr = sorted(list(map(int,input().split()))) # 각 병에 남아있는 용량

s = 0
e = n-1
remain = 0
cnt = 0

while s <= e: # s와 e가 교차되면 멈춘다
    if arr[e] == x:
        cnt += 1
        e -= 1
        continue
    
    if s == e:
        remain += 1 # 짜투리를 하나 추가한다.
        break
        
    if arr[s] + arr[e] >= (x/2):
        cnt += 1
        e -= 1
        s += 1
    else:
        remain += 1
        s += 1 # 수가 커진다.

print(cnt+remain//3)
