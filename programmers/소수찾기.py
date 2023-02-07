# 프로그래머스 lv 2
# 소수찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    per = []
    for i in range(1,len(numbers)+1):
        per += list(permutations(nums,i))
    
    new_nums = [int("".join(p)) for p in per]
    for n in new_nums:
        if n<2:
            continue
        check = True
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                check = False
                break
        if check:
            answer.append(n)
            
    return len(set(answer))
