# 프로그래머스 lv 2
# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total = yellow + brown
    for b in range(1,total+1):
        if (total/b) % 1 == 0:
            a = total / b
            if a >= b:
                if 2*a + 2*b == brown + 4:
                    return [a,b]
    return answer
