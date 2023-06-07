# 프로그래머스 lv 4 도둑질
# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    # 1번 집을 터는 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):  # 마지막 집은 털지 못함
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])

    # 1번 집을 안터는 경우
    dp2 = [0] * len(money)
    dp2[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])

    return max(dp1[-2], dp2[-1])
