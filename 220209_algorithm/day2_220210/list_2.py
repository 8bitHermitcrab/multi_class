n, m = int(input())

borad = [list(map(int, input().split())) for _ in range(n)]

print(borad)

""" 
입력값
5
0 1 3 2 4
3 4 2 3 4
2 1 2 3 4
2 4 5 2 3
2 1 2 3 4

출력값
[[0, 1, 3, 2, 4], [3, 4, 2, 3, 4], [2, 1, 2, 3, 4], [2, 4, 5, 2, 3], [2, 1, 2, 3, 4]] 
"""