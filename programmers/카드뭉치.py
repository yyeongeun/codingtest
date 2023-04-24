# 프로그래머스 lv1 카드 뭉치
# https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque

def solution(cards1, cards2, goal):
    card1 = deque(list(cards1))
    card2 = deque(list(cards2))
    
    for g in goal:
        if card1 and g == card1[0]:
            card1.popleft()
        elif card2 and g == card2[0]:
            card2.popleft()
        else:
            return "No"

    return "Yes"
