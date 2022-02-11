# 리스트

a = []

for _ in range(2):
    number = list(map(int, input().split()))
    a.append(number)


b = []

for _ in range(2):
    number = list(map(int, input().split()))
    b.append(number)


a = [list(map(int, input().split())) for _ in range(2)]
b = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    for j in range(4):
        print(a[i][j] * b[i][j], end=" ")
    print()