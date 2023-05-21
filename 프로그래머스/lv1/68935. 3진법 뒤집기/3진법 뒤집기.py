def solution(n):
    a = []
    while n:
        a.append(n%3)
        n = n//3
        
    answer = 0
    for i in range(len(a)):
        answer += a[i] * 3**(len(a)-i-1)
    
    return answer