# 프로그래머스 lv 3 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    puddles = [[q,p] for [p,q] in puddles]
    dq = [[0]*(m+1) for _ in range(n+1)]
    dq[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1: continue
            if [i,j] in puddles:
                dq[i][j] = 0
            else:
                dq[i][j] = (dq[i][j-1] + dq[i-1][j]) % 1000000007

    return dq[n][m]
