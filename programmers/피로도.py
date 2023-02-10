# 프로그래머스 lv 2
# 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for d in permutations(dungeons,len(dungeons)):
        limit = k
        cnt = 0
        for min_cost, cost in d:
            if limit >= min_cost:
                limit -= cost
                cnt += 1
            answer = max(answer,cnt)
    
    return answer
