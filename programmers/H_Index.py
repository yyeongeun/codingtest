# 프로그래머스 lv 2
# H_Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
