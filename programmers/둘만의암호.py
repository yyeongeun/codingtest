# 프로그래머스 lv 1 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for a in alpha:
        if a in skip:
            alpha = alpha.replace(a,"")
    
    for i in s:
        result = alpha[(alpha.index(i)+index)%len(alpha)]
        answer += result
    
    return answer
