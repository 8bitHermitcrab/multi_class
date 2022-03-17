# 스도쿠 채점
# dfs 공부하기


# 맨 처음에는 각 테스트 케이스의 개수가 주어진다.
T = int(input())
sudoku = [list(map(int, input().split())) for _ in range(9)]
board = [(x, y) for x in range(9) for y in range(9) if sudoku[x][y] == 0]

value = 0
result = {0 : "CORRECT", 1 : "INCORRECT"}

# 행에서 합 45 확인
def CheckRow(x, value):
    value += sudoku[x]
    if value == 45:
        result[0]
    else:
        result[1]
    return

# 열에서 합 45 확인
def CheckCol(y, value):
    for i in range(9):
        value += sudoku[i][y]
        if value == 45:
            result[0]
        else:
            result[1]
    return

# 3*3에서 합 45 확인
def CheckMid(x, y, value):
    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            value += sudoku[nx+i][ny+j]
            if value == 45:
                result[0]
            else:
                result[1]
    return

for i in range(9):
    if CheckRow() == result[0] and CheckCol() == result[0] and CheckMid() == result[0]:
        result = result[0]
    else:
        result = result[1]

print(f'Case {T}: {result}')

'''
# 행 확인
def CheckRow(x, value):
    if value == sudoku[x]:
        return 'INCORRECT'
    return 'CORRECT'
# 열 확인
def CheckCol(y, value):
    for i in range(9):
        if value == sudoku[i][y]:
            return 'INCORRECT'
    return 'CORRECT'

# 3*3 확인
def CheckMid(self, result):
    temp = 0
    for i in range(3):
        for j in range(3):
            temp += sudoku[i][j]
            if temp == 45:
                result = 'CORRECT'
            else:
                result = 'INCORRECT'
    return result

    https://dojinkimm.github.io/problem_solving/2019/10/16/boj-2580-sudoku.html
'''

'''
# 각 테스트 케이스는 9개의 줄로 이루어져 있으며, 공백으로 구분된다.
for n in range(9):
    lines = list(map(int, input().split()))
# 3x3씩 1~9가 들어가있는지 확인하기
    for i in range(3*n, (3*n+3)):
        for j in range(3*n, (3*n+3)):
            if lines[i][j] in stoku:
                stoku.pop(lines[i][j])
                result = 'CORRECT'
                if stoku == 0:
                    continue
            else:
                result = 'INCORRECT'

print(f'Case {T}: {result}')
'''

'''
t = int(input())

for _ in range(t):
    rows = [int(input().split()) for _ in range(9)]

    if rows.sum() == 45:
        result = 'CORRECT'
    else:
        result = 'INCORRECT'

print(f'Case {t}: {result}')
'''