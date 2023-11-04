# 백준 1991번 트리 순회
# 트리 DFS 알고리즘
# https://www.acmicpc.net/problem/1991

# 전위 순회
def preOrder(start):
    if start != - 18:
        print(chr(start+64), end = "") # 부모
        preOrder(tree[start][0]) # 왼쪽 자식
        preOrder(tree[start][1]) # 오른쪽 자식
# 중위 순회
def inOrder(start):
    if start != -18:
        inOrder(tree[start][0]) # 왼쪽 자식
        print(chr(start+64), end = "") # 부모        
        inOrder(tree[start][1]) # 오른쪽 자식
# 후위 순회
def postOrder(start):
    if start != -18:
        postOrder(tree[start][0]) # 왼쪽 자식
        postOrder(tree[start][1]) # 오른쪽 자식       
        print(chr(start+64), end = "") # 부모

n = int(input()) # 노드 개수
tree = [[] for _ in range(n+1)] #아스키 코드 127까지 있음

for _ in range(n):
    a, b, c = input().split() # 노드, 왼쪽 자식, 오른쪽 자식
    # 노드 이름 A~ 알파벳 대문자라 탐색 어려우므로 아스키 코드로 변경
    # ord(A) = 65, ord(.) = 18
    a, b, c = ord(a)-64, ord(b)-64, ord(c)-64
    # 그래프 관계 연결시키기
    tree[a].append(b)
    tree[a].append(c)

preOrder(1)
print()
inOrder(1)
print()
postOrder(1)
