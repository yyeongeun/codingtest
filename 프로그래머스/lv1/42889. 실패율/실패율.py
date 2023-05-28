def solution(N, stages):
    k = len(stages)
    s = []
    
    for i in range(1,N+1): # 스테이지 번호
        c = 0
        for j in range(len(stages)):
            if stages[j] == i:
                c += 1 # 각 스테이지 별 클리어하지 못한 사용자 수
        if c == 0:
            s.append(0)
        else:
            s.append(c/k)
        k -= c
        
    a = sorted(s,reverse=True)
    answer = []
    
    for i in range(len(a)):
        answer.append(s.index(a[i])+1)
        s[s.index(a[i])] = 2 # 실패율 최대 1. 2로 설정해서 중복방지
        
    return answer