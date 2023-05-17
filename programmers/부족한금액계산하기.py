# 프로그래머스 lv 1 부족한 금액 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer += price*i
    answer -= money
    
    if answer < 0 :
        return 0
    else:
        return answer
