# 기타 자료형 - 형성평가 6


# 초기화
players = input().split()
fouls = {}

for player in players:
    # 이미 파울을 했나?
    if player in fouls:
        fouls[player] += 1
    # 파울을 한 번도 안 했나?
    else:
        fouls[player] = 1

# 파울 가장 적게 한 선수 뽑기
min_foul = min(fouls.values())

for player, foul in fouls.items():
    if foul == min_foul:
        print(player)

print(min_foul)




'''

# 초기화
players = input().split()
fouls = {}

for player in players:
    # 이미 파울을 했나?
    if player in fouls:
        fouls[player] += 1
    # 파울을 한 번도 안 했나?
    else:
        fouls[player] = 1

'''
