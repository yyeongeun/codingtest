# 프로그래머스 lv 1 나머지 한 점
# https://school.programmers.co.kr/learn/courses/18/lessons/1878

def solution(v):
    x = []
    y = []
    answer = []
    
    for i in v:
        if i[0] not in x:
            x.append(i[0])
        else:
            x.remove(i[0])
        if i[1] not in y:
            y.append(i[1])
        else:
            y.remove(i[1])
            
    answer = x+y

    return answer
