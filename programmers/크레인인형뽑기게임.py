# 프로그래머스 lv 1 크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    doll = []
    
    for m in moves:
        for b in board:
            if b[m-1] >= 1: # 각 줄마다 m줄에 있는 인형이 있다면
                if doll and doll[-1] == b[m-1]: # 가장 마지막 인형과 값이 같다면
                    answer += 2
                    del doll[-1]
                else:
                    doll.append(b[m-1])
                b[m-1] = 0 # 인형 없애기
                break # for b in board 중단
    
    return answer
