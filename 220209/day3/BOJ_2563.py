# 색종이

# 도화지 100x100
# 색종이 10x10

# 색종이 수
# 좌표값 + 색종이10


# 도화지를 만든다. (0으로)
paper = [[0]*100 for _ in range(100)]

# 입력, 좌표받아오기
# 색종이 개수 받기
n = int(input())

# 색종이 칠하기
for _ in range(n):
    x, y = map(int, input().split())
    # 색종이 2차원 리스트 돌기
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            # 도화지가 빈칸이면
            # if paper[i][j] == 0:
            paper[i][j] = 1 # 색칠
            # else:
            #     continue

# 영역의 넓이 출력(도화지에서 1인 부분을 그냥 다 더한다)
total = 0
for i in range(100):
    for j in range(100):
        total += paper[i][j]

# total = sum(sum(line) for line in paper)

print(total)