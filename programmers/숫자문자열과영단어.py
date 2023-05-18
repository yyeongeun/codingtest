# 프로그래머스 lv 1 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    alpha = ["zero","one","two","three","four","five","six","seven","eight","nine"]

    for i,a in enumerate(alpha):
        if a in s:
            s = s.replace(a,str(i))

    return int(s)
