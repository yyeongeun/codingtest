# 2309번 일곱 난쟁이
## https://www.acmicpc.net/problem/2309
### try 5 times

import sys

# 방법1
heights = []
for i in range(9):
    heights.append(int(sys.stdin.readline())) # 한줄에 여러 입력 값 

# 방법2
# data = lambda: sys.stdin.readline().rstrip() # 오른쪽 공백 삭제
# heights = [int(data()) for _ in range(9)]

# 방법3
# list = [int(input()) for i in range(9)]

# 동일
total = sum(heights)
one = 0
two = 0

for i in range(9):
    for j in range(i+1, 9):
        if total - (heights[i] + heights[j]) == 100:
            one, two = heights[i], heights[j]
            break

heights.remove(one)
heights.remove(two)
heights.sort()

for i in heights:
    print(i)
