# 2805번
# https://www.acmicpc.net/problem/2805

n, m = map(int,input().split())
tree = sorted(list(map(int,input().split())))

start, end = 1, max(tree)

while start <= end:
    mid = (start+end)//2
    answer = 0
    
    for i in tree:
        if i >= mid:
            answer += i-mid
    if answer >= m :
        start = mid+1
    else:
        end = mid-1
print(end)
