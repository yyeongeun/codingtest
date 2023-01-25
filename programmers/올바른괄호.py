# 프로그래머스 lv 2
# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    
    stack  = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        answer = True
    else:
        answer = False
    

    return answer
