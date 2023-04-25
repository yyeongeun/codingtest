# 프로그래머스 lv 1 명예의 전당(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    answer = []
    stack = [] #명예의 전당 리스트
    for s in score:
        if len(stack) < k: # 상위 k번째 이내이면 명예의 전당
            stack.append(s)    
        else:
            if min(stack) < s:
                stack.remove(min(stack))
                stack.append(s)
        
        answer.append(min(stack))
    return answer
