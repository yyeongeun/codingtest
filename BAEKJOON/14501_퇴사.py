# 백준 14501번 퇴사
# https://www.acmicpc.net/problem/14501

def recur(day,total):
    global answer
    if day > n-1: # day = 0일부터 n-1일까지
        if day > n: return
        answer = max(total,answer)
        return
    
    # 상담 하는 경우
    recur(day+list_a[day][0],total+list_a[day][1])
    # 상담 안하는 경우
    recur(day+1, total)

n = int(input()) # n일째
list_a = [list(map(int,input().split())) for _ in range(n)] # t,p
answer = 0
recur(0,0) #0일부터 시작
print(answer)
