# 프로그래머스 lv 1 순열 검사
# https://school.programmers.co.kr/learn/courses/18/lessons/1877

def solution(arr):
    answer = True
    
    arr.sort()
    for i in range(len(arr)):
        if (i+1 != arr[i]):
            answer = False
            return False
        
    return answer
