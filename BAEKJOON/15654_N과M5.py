# 백준 N과 M(5)
# https://www.acmicpc.net/problem/15654

def recur(number):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            arr.append(list_n[i])
            recur(number+1)
            arr.pop()
            visited[i] = 0

n, m = map(int,input().split())
list_n = list(map(int,input().split()))
list_n.sort()

visited = [0 for _ in range(n+1)]
arr = []
recur(0)
