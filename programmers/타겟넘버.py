# 프로그래머스 lv 2
# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

answer = 0
def dfs(depth,numbers,target,total):
    global answer
    n = len(numbers)
    if depth == n and target == total:
        answer += 1
        return
    if depth == n:
        return
    
    dfs(depth+1,numbers,target,total+numbers[depth])
    dfs(depth+1,numbers,target,total-numbers[depth])
    
def solution(numbers,target):
    global answer
    dfs(0,numbers,target,0)
    return answer
