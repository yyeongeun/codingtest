# 10870번 피보나치 수 5
## https://www.acmicpc.net/problem/10870
### try 3 times

n = int(input())
fibonacci = [0,1]

# 리스트 중 가장 오른쪽 두 숫자를 계속 더하는 for문
for i in range(2,n+1):
    num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(num)

# for문의 가장 마지막 n -> n-1번째와 n-2번째 더한 값 = 리스트의 n번째 값
print(fibonacci[n])


# 다른 풀이 - 재귀 함수 사용
# n = int(input())
# def fibonacci(n):
# 	if n <= 1:
#     	return n
# 	return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(n))
