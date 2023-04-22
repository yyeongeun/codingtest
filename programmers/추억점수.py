# 프로그래머스 lv1 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []

    for p in photo:
        total = 0
        for i in range(0,len(p)):
            for j in range(0,len(name)):
                if p[i] == name[j] :
                    total += yearning[j]
    
        answer.append(total)
    
    return answer
