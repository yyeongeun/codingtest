# 프로그래머스 lv 2
# 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    
    answer = [0]*len(prices)
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break

    return answer
