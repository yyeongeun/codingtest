# 프로그래머스 lv1 음양 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=python3
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
