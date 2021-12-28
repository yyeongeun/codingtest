# 이진수
## https://www.acmicpc.net/problem/3460
### try 5 times

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    # 양의 정수 입력시 이진수로 변환
    # 프로그래밍 언어에서 숫자 앞에 0b를 붙이므로, 2번째 값부터 숫자
    n = bin(int(input()))[2:] # 문자열
    
    # 이진수는 오른쪽 숫자부터 제일 작은 숫자이다. (최하위 비트)
    # 최하위 비트의 위치는 0이라고 했으므로 가장 왼쪽으로 바꿔줘야한다.
    # 범위를 거꾸로 선언한다.
    for idx, val in enumerate(n[::-1]):
        if val == '1': #n이 문자열이니까
            print(idx, end=' ')
#    for i in range(len(n)):
#        if n[-i-1] == '1':
#            print(i, end=' ')

# 리스트 - 범위를 거꾸로 선언하는 방법
#for i in range(len(arr)-1,-1,-1):
#    print(arr[i], end=' ')
# 리스트 - 출력을 거꾸로 선언하는 방법
#for i in range(len(arr)):
#    print(arr[-i-1], end=' ')
