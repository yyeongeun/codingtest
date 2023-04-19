# 백준 1713번 후보 추천하기
# https://www.acmicpc.net/problem/1713

n = int(input()) #사진들 개수
c = int(input()) # 전체 학생의 총 추천 횟수
vote = list(map(int,input().split())) # 추천받은 학생을 나타내는 번호

pic = [] # 사진틀
num_pic = [] # 사진틀 추천개수

for v in vote:
    if v in pic: # 이미 다른 학생의 추천을 받은 경우 횟수만 증가
        idx = pic.index(v)
        num_pic[idx] += 1
    else:
        if len(pic) >= n: # 비어있는 사진틀이 없는 경우
            idx = num_pic.index(min(num_pic))
            del pic[idx]
            del num_pic[idx]
        pic.append(v)
        num_pic.append(1)

pic.sort()
print(' '.join(map(str,pic)))
