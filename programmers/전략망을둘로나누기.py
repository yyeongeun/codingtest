# 프로그래머스 lv 2
# 전력망을 둘로 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def bfs(start,visited,graph):
    queue = deque([start])
    result = 1 #연결된 노드수
    visited[start] = True #시작 노드 방문 처리
    while queue: #bfs 수행
        now = queue.popleft()
        
        for i in graph[now]: #now 노드와 연결된 노드에 대해서
            if visited[i] == False: #방문하지 않았을 경우만
                result += 1
                queue.append(i)
                visited[i] = True
                
    return result
        

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
            
    for start,not_visit in wires:
        visited = [False]*(n+1)
        visited[not_visit] = True
        # 해당 노드 끊었을 때, 한쪽 영역의 노드 수 result 구하기
        result = bfs(start,visited,graph)
        # 기존 result와 현재 result 차이 비교해서 최소값 구하기
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
        
    return answer
