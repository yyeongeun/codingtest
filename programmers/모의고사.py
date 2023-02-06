# 프로그래머스 lv 1
# 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    total1,total2,total3 = 0,0,0
    
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        
        if num1[s1] == answers[i]:
            total1 += 1
        if num2[s2] == answers[i]:
            total2 += 1
        if num3[s3] == answers[i]:
            total3 += 1
            
    k = max(total1,total2,total3)
    answer = []
    
    if k == total1:
        answer.append(1)
    if k == total2:
        answer.append(2)
    if k == total3:
        answer.append(3)
        
    return answer
