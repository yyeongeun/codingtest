# 프로그래머스 lv 1 가장 가까운 같은 글자
# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    list_a = []
    for i in s:
        if i in list_a:
            answer.append(list_a[::-1].index(i)+1)
        else:
            answer.append(-1)
        list_a.append(i)
    return answer
