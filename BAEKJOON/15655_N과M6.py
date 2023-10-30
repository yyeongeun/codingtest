# 백준 15655번 N과 M(6)
# https://www.acmicpc.net/problem/15655

def recur(number):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(number,n):
        if list_n[i] not in arr:
            arr.append(list_n[i])
            recur(i+1)
            arr.pop()

        
n, m = map(int,input().split())
list_n = list(map(int,input().split()))
list_n.sort()
arr = []
recur(0)
