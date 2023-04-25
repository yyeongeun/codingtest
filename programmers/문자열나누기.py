# 프로그래머스 lv 1 문자열 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    cnt1, cnt2 = 0,0
    
    for i in s:
        if cnt1 == cnt2:
            answer += 1
            k = i
        if k == i:
            cnt1 += 1
        else:
            cnt2 += 1
    
    return answer
