# 프로그래머스 lv 1 과일 장수
# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    score.sort() # 사과 점수에 따라 정렬
    cnt = (len(score)%int(m)) # 버리는 사과 개수
    if cnt >= 1:
        for i in range(cnt):# 사과 버리기
            score.remove(score[0])
    
    # 최대이익 계산
    for i in range(0,int(len(score)/int(m))): # 최대이익
        answer += (score[m*i])*m
            
    return answer
