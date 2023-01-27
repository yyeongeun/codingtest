# 프로그래머스 lv 2
# 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
  numbers = list(map(str,numbers))
  numbers.sort(key = lambda x:x*3, reverse=True)
  return str(int(''.join(numbers)))
