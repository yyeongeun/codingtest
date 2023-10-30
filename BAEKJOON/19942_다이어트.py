# 백준 19942번 다이어트
# https://www.acmicpc.net/submit/19942/68623910

def recur(idx,p,f,s,v,price):
    global answer
    global used
    global answer_used
    
    if p >= mp and f >= mf and s >= ms and v >= mv: # 최소값 만족
        if answer > price: # 최소 비용이라면
            answer = min(answer,price)
            answer_used = []
            for i in used:
                answer_used.append(i)
    if idx == n:
        return
        
    used.append(idx+1) # 사용한 재료 추가
    # 재료 사용했다면        
    recur(idx+1, p+list_a[idx][0], f+list_a[idx][1], s+list_a[idx][2], v+list_a[idx][3], price+list_a[idx][4])
    used.pop() # 사용한 재료 삭제
    # 재료 사용안했다면
    recur(idx+1, p, f, s, v, price)
    
# 식재료 개수
n = int(input())
# 단백질, 지방, 탄수화물, 비타민의 최소 영양성분
mp,mf,ms,mv = map(int,input().split())
# 각 식재료의 단백질, 지방, 탄수화물, 비타민, 가격
list_a = [list(map(int,input().split())) for _ in range(n)]
answer = 1e9
used = [] # 사용한 재료
answer_used = [] # 최소값 만족하는 사용한 재료

recur(0,0,0,0,0,0)
answer_used.sort() # 정렬 후 프린트
if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)
