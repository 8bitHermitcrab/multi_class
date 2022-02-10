# 하얀 칸

# 체스판 만들기
board = [list(input()) for _ in range(8)]
# print(board)
total = 0
# 체스판을 모두 돌아다니면서 조건 확인
# 하얀 칸 and 말이 있나? 순회+조건(하얀, F)?
for i in range(8):
    for j in range(8):
        # 짝짝/홀홀 and 말 있나?
        # i % 2 == 0 and j % 2 == 0
        if i % 2 == j % 2 and board[i][j] == 'F':
            total += 1
print(total)



##print(sum(input()[i % 2 :: 2].count('F') for i in range(8)))



""" 
chase_plat=[]

for _ in range(8):
    slot = list(input())
    chase_plat.extend(slot)

print(chase_plat) 
"""


# if [i][j] == 'F'
# sum_f = borad.count('F')
# sum_f =+ sum_f
# print(sum_f)

# # print(borad)
# for i in range(8):
#     for j in range(8):
        # if borad[i][j] == 'F':
#             sum_f = borad[i][j].count('F')
#             sum_f =+ sum_f
#         else:
#             continue
# print(sum_f)

# if borad[i] == 'F':
#     count_f = borad.count('F')
#     print(count_f)

# borad = [list(map(int, input().split())) for _ in range(n)]