# 프로그래머스 lv1 약수의 개수와 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    result = 0
    for n in range(left,right+1):
        answer = 0
        # 약수 : 나누어 떨어지는 숫자
        for i in range(1,n+1):
            if n%i == 0:
                answer += 1
        if answer%2 == 0: #짝수
            result += n
        else:
            result -= n
        
    return result
