# 직사각형 네개의 합집합의 면적 구하기

# 전체 좌표
square = [[0] * 101 for _ in range(101)]

# 입력값 x1 y1 x2 y2
for _ in range(4):
    x1, y1, x2, y2  = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            square[i][j] = 1

total = 0
for i in range(100):
    for j in range(100):
        total += square[i][j]

print(total)