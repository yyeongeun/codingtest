#15651번
#https://www.acmicpc.net/problem/15651

N, M = map(int,input().split())
ans = []
def back():
    if len(ans) == M:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,N+1):
            ans.append(i)
            back()
            ans.pop()
    
back()
