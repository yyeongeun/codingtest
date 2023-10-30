# 백준 15656번 N과 M(7)
# https://www.acmicpc.net/problem/15656

def recur():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(n):
        arr.append(list_n[i])
        recur()
        arr.pop()
    
n, m = map(int,input().split())
list_n = list(map(int,input().split()))
list_n.sort()
arr = []
recur()
