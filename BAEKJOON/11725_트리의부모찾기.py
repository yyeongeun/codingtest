# 백준 11725번 트리의 부모 찾기
# 트리 DFS 알고리즘
# https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(99999)

def recur(node, prv):
    parent[node] = prv # 해당 노드의 부모 = 이전 노드
    for nxt in tree[node]:
        if nxt == prv: # 역주행 방지, 재계산 금지
            continue
        recur(nxt, node)
    
n = int(input()) # 노드 개수
tree = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1): # 간선의 개수 = n-1
    a, b = map(int,input().split()) # 정점1, 정점2
    # 양방향 = 누가 부모이고 자식인지 모르기 때문이다.
    tree[a].append(b)
    tree[b].append(a)

recur(1,0)
for answer in parent[2:]:
    print(answer)
