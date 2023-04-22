# 프로그래머스 lv1 달리기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    idx = {i : players for i, players in enumerate(players)}
    p = {players : i for i, players in enumerate(players)}

    for i in callings:
        loc = p[i] # 현재 선수 위치
        loc2 = loc-1 # 한칸 앞 위치
        i2 = idx[loc2] # 앞선수
        
        idx[loc] = i2 # 현재 선수를 앞선수로 바꾸기
        idx[loc2] = i # 앞선수를 현재 선수으로 바꾸기
        
        p[i] = loc2 # 현재 선수를 loc2로 바꾸기
        p[i2] = loc # 앞선수를 loc로 바꾸기

    return list(idx.values())
