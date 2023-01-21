# 2110번
# https://www.acmicpc.net/problem/2110

n, c = list(map(int,input().split()))
house = []
for i in range(n):
    house.append(int(input()))
house.sort()
start, end = 1, house[-1]-house[0]
result = 0


while start <= end:
    mid = (start+end)//2
    current = house[0]
    cnt = 1
    
    for i in range(1,n):
        if house[i] >= current + mid:
            cnt += 1
            current = house[i]
    if cnt >= c:
        start = mid+1
        result = mid
    else:
        end = mid-1
        
print(result)
