#1296번
#https://www.acmicpc.net/problem/1296

### 보통 정답
N = input().upper()
team = sorted([input() for _ in range(N)])
max_i = max_p = 0

for i in range(N):
  L = N.count('L') + team[i].count('L')
  O = N.count('O') + team[i].count('O')
  V = N.count('V') + team[i].count('V')
  E = N.count('E') + team[i].count('E')
  p = ((L+O) * (L+V) * (L+E) × (O+V) * (O+E) * (V+E)) % 100
  
  if max_p > p :
    max_p = p
    max_i = i
  
print(team[max_i])


### 내 정답
name = input().upper() # 연두의 영어 이름
N = int(input()) # 팀이름 후보 개수
team = [] #팀이름 후보
for _ in range(N):
  num = input().upper()
  team.append(num)

team.sort() #팀 이름 사전순으로 정렬
# LOVE 개수
L = []
O = []
V = []
E = []

# 연두 이름에서 LOVE 개수 찾기
for i in range(len(name)):
    try :
        if name[i].index('L') >= 0:
            L.append(1)
    except:
        L.append(0)
    
    try:
        if name[i].index('O') >= 0:
            O.append(1)
    except:
        O.append(0)
    
    try:
        if name[i].index('V') >= 0:
            V.append(1)
    except:
        V.append(0)
        
    try:    
        if name[i].index('E') >= 0:
            E.append(1)
    except:
        E.append(0)

name_L = sum(L)
name_O = sum(O)
name_V = sum(V)
name_E = sum(E)

cnt = [] 
for j in range(N):
  L = []
  O = []
  V = []
  E = []
  for i in range(len(team[j])): 
    try :
      if team[j][i].index('L') >= 0:
        L.append(1)
      except:
        L.append(0)
    try:
      if team[j][i].index('O') >= 0:
        O.append(1)
      except:
        O.append(0)
    try:
      if team[j][i].index('V') >= 0:
        V.append(1)
      except:
        V.append(0)
    try:
      if team[j][i].index('E') >= 0:
        E.append(1)
      except:
        E.append(0)
            
  team_L = sum(L)
  team_O = sum(O)
  team_V = sum(V)
  team_E = sum(E)
  total_L = name_L + team_L
  total_O = name_O + team_O
  total_V = name_V + team_V
  total_E = name_E + team_E
            
  answer = ((total_L+total_O)*(total_L+total_V)*(total_L+total_E)
           *(total_O+total_V)*(total_O+total_E)*(total_V+total_E))%100
  cnt.append(answer)

print(team[cnt.index(max(cnt))])
