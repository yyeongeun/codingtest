# 프로그래머스 lv 2
# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp = 0
    truck_bridge_deque = deque(bridge_length * [0])
    truck_weights_deque = deque(truck_weights)
    
    while len(truck_bridge_deque):
        answer += 1
        temp -= truck_bridge_deque[0]
        truck_bridge_deque.popleft()
        
        if truck_weights_deque:
            if temp + truck_weights_deque[0] <= weight:
                temp += truck_weights_deque[0]
                truck_bridge_deque.append(truck_weights_deque.popleft())
            else:
                truck_bridge_deque.append(0)
                
    return answer
