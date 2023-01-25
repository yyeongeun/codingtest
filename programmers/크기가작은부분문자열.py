# 프로그래머스 lv 1
# 크기가 작은 부분 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    
    if len(p) <= len(t):
        for i in range(len(t)-len(p)+1):
            if t[i:i+len(p)] <= p[0:len(p)]:
                answer += 1
        

    return answer
