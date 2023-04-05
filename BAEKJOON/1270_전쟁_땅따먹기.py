# 1270번 전쟁-땅따먹기
# https://www.acmicpc.net/problem/1270
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
for i in range(N):
    A = list(map(int, input().split()))
    count = A.pop(0) #병사수
    counter = Counter(A).most_common(n=1) #가장 많은 병사.땅을 지배한 병사
    
    if int(count) / counter[0][1] < 2.0: #과반수 넘는다면
        print(counter[0][0])
    else:
        print('SYJKGW')
