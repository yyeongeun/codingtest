def solution(numbers):
    answer = []
    
    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)):
            if numbers[i] != numbers[j] or (numbers[i] == numbers[j] and i != j):
                n = numbers[i] + numbers[j]
                if n not in answer: # 중복제거
                    answer.append(numbers[i] + numbers[j])

    answer.sort() # 오름차순 정렬
    
    return answer