# 프로그래머스 lv1 콜라 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    while n >= a:
        remain_bottle = n%a
        n = (n//a)*b
        answer += n
        n += remain_bottle
        
    return answer
