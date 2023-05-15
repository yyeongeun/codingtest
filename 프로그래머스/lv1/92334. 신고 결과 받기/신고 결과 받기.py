# defaultdict = dict 입력형식 지정 set or int
from collections import defaultdict

def solution(id_list,report,k):
    answer = []
    
    report = list(set(report)) #report 중복제거
    user = defaultdict(set) #신고한 id : 신고받은 id
    cnt = defaultdict(int) #신고한 사람별 신고 횟수
    
    for r in report:
        a,b = r.split() #신고 한 사람, 신고 받은 사람
        user[a].add(b) # {신고한 사람 : 신고 받은 사람들}
        cnt[b] += 1 # {신고받은 사람 : 신고 받은 횟수}
        
    for i in id_list:
        result = 0
        for u in user[i]: #id별
            if cnt[u] >= k: #id별 신고횟수 조사
                result += 1
        answer.append(result)
        
    return answer