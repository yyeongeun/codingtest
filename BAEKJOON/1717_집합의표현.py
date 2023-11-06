# 백준 1717번 집합의 표현
# 유니온 파인더 알고리즘 풀이
# https://www.acmicpc.net/problem/1717

def _union(a,b):
    # 유니온 최적화
    # 1. 머리끼리 합치기. 쓸데없는 find를 안하도록
    a = _find(a)
    b = _find(b)
    # 2. depth가 큰 집합에 작은 집합 붙이기. 
    if a == b:
        return
    if rank[a] < rank[b]:
        par[a] = b # a의 부모 = b로 붙이기
    elif rank[b] < rank[a]:
        par[b] = a
    else:
        par[a] = b # 반대로 해도 상관없음
        rank[b] += 1 # b의 depth가 1개 증가

def _find(a):
    if par[a] != a:
        par[a] =  _find(par[a])
    return par[a]

n,m = map(int,input().split()) # 집합개수, 연산개수
rank = [0 for _ in range(n+1)] # 점프할 수 있는 칸 = 0칸에서 시작 = depth
par = [i for i in range(n+1)] # 스스로가 부모인 상태에서 시작

for _ in range(m):
    x,a,b = map(int,input().split())
    if x == 0: # 두 집합 합하기 union
        _union(a,b)
    if x == 1: # 두 집합이 같은 집합인가? find
        if _find(a) == _find(b):
            print("YES") 
        else:
            print("NO")
