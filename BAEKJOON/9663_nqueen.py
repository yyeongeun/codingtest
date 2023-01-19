#9663번
#https://www.acmicpc.net/problem/9663

n = int(input())
row = [0]*n
ans = 0

def is_promising(x):
    for i in range(x):
        if (row[x]==row[i]) or (abs(row[x]-row[i]) == abs(x-i)):
            return False
    return True
    
def nqueen(x):
    global ans
    
    if x == n:
        ans+=1
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                nqueen(x+1)
nqueen(0)
print(ans) 
