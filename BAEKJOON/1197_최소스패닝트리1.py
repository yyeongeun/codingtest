# 백준 1197번 최소 스패닝 트리
# 크루스칼(유니온파인드) 풀이
# https://www.acmicpc.net/problem/1197
# union 최적화
def _find(x):
    while par[x] != x:
        x = par[x]
    return x

def _union(a,b):
    a = _find(a)
    b = _find(b)
    
    if a == b:
        return
    
    if rank[a] < rank[b]:
        par[a] = b
    elif rank[b] < rank[a]:
        par[b] = a
    else:
        par[a] = b
        rank[b] += 1

v,e = map(int, input().split()) # 정점의 개수, 간선의 개수
link = [list(map(int,input().split())) for _ in range(e)] # 모든 링크 가져오기
link.sort(key=lambda x:x[2])# 가중치 기준으로 정렬
par = [i for i in range(1_000_001)] # 부모
rank = [0 for _ in range(1_000_001)] # union 최적화

answer = 0
for i in range(e):
    a = link[i][0]
    b = link[i][1]
    weight = link[i][2]
    
    # 같은 부모인지 찾기    
    a = _find(a)
    b = _find(b)
    # 부모 같지 않을 때만 합해주기
    if a != b:
        _union(a,b)
        answer += weight
    else:
        continue
        
print(answer)
