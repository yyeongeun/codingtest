def solution(today, terms, privacies):
    answer = []
    time_dic = dict()

    year,month,day = int(today[0:4]),int(today[5:7]),int(today[8:]) #오늘의 연, 월, 일
    
    for term in terms:
        case = term[0] # 유형
        time_dic[case] = int(term[2:]) # 유형별 기간 dic 저장

    for i in range(len(privacies)):
        data, case = privacies[i].split()
        p_year, p_month, p_day = int(data[0:4]),int(data[5:7]),int(data[8:10]) # 시간
        
        p_month += time_dic[case] #유형별 기간 p_month에 추가해주기
        
        while p_month > 12: # 12월 넘으면 month-12, year+1
            p_month -= 12
            p_year += 1
        
        # 유효기간이 today의 연,월,일보다 작아야 보관가능하다. +1
        if p_year > year:
            continue
            
        elif p_year == year:
            if p_month > month:
                continue
            elif p_month == month:
                if p_day > day:
                    continue
                    
        answer.append(i+1) # 인덱스 0부터 시작하기 때문에
        
    return answer