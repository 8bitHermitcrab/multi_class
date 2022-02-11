# 스도쿠 채점

# 맨 처음에는 각 테스트 케이스의 개수가 주어진다.
T = int(input())
result = ''
stoku = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 각 테스트 케이스는 9개의 줄로 이루어져 있으며, 공백으로 구분된다.
for n in range(9):
    lines = list(map(int, input().split()))
# 3x3씩 1~9가 들어가있는지 확인하기
    for i in range(3*n, (3*n+3)):
        for j in range(3*n, (3*n+3)):
            if lines[i][j] in stoku:
                stoku = stoku.pop(lines[i][j])
                result = 'CORRECT'
                if stoku == 0:
                    continue
            else:
                result = 'INCORRECT'

print(f'Case {T}: {result}')