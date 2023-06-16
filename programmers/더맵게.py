-- 프로그래머스 lv 2 더 맵게
-- https://school.programmers.co.kr/learn/courses/30/lessons/42626#

import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)

    cnt = 0
    while heap[0] < K:
        try
            heapq.heappush(heap, heapq.heappop(heap)+heapq.heappop(heap)*2)
        except IndexError:
            return -1
        cnt += 1

    return cnt
