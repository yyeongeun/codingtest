# 프로그래머스 lv1 햄버거 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    #1,2,3,1 빵, 야채, 고기, 빵
    stack = []
    ham = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            ham += 1
            del stack[-4:]
    
    return ham
