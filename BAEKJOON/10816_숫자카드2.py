# 10816번
# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

n = int(input())
mycard = sorted(list(map(int,input().split())))
m = int(input())
test = list(map(int,input().split()))

count = {}
for c in mycard:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

def binarySearch(arr, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid+1, end)
    else:
        return binarySearch(arr, target, start, mid-1)
    
for target in test:
    print(binarySearch(mycard, target, 0, n-1), end=" ")
