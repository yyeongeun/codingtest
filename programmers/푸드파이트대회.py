# 프로그래머스 lv1 푸드 파이트 대회
# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    num1 = ''
    answer = ''
    
    for i in range(1,len(food)):
        a = food[i]//2 # 몫(한 선수당)
        num1 += str(i)*a
        # a만큼 i를 출력해야함
    
    answer += num1
    answer += str(0)
    answer += num1[::-1]

    return answer
