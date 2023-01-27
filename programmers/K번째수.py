# 프로그래머스 lv 1
# K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):

    answer = []

    for p in range(len(commands)):
        i = commands[p][0]
        j = commands[p][1]
        k = commands[p][2]
        array1 = array[i-1:j]    
        array1.sort()
        answer.append(array1[k-1])

    return answer
