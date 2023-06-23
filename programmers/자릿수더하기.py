# 프로그래머스 lv 1 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/18/lessons/1876

def solution(n): 
    a = list(map(int,str(n)))
    return sum(a)
