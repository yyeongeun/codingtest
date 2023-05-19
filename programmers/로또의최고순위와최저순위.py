# 프로그래머스 lv 1 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    cnt = 0 # 당첨 개수
    zero = lottos.count(0) # 0 개수
    
    for l in lottos:
        if l in win_nums: # 당첨
            cnt += 1
    n_max = cnt+zero # zero를 모두 당첨
    n_min = cnt # zero가 모두 미당첨

    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer = [rank[n_max],rank[n_min]]
    
    return answer
