# 프로그래머스 lv 1 소수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12977

import itertools
def solution(nums):
    answer = 0
    # 3개를 선택하는 경우의 수 nC3
    stack = list(itertools.combinations(nums,3))
    
    sum_stack = []
    for s in stack:
        sum_stack.append(sum(s))
    set(sum_stack) #중복제거    
    
    # 소수구하기
    for i in sum_stack:
        cnt = 0
        for j in range(1,i//2+1):
            if i%j == 0:           
                cnt += 1
        if cnt == 1: #소수
            answer += 1

    return answer
